import asyncio
import os
from typing import Any, Awaitable, Callable


Judge0Job = Callable[[], Awaitable[Any]]


class Judge0ExecutionQueue:
    """
    FIFO queue with a fixed worker pool for Judge0 executions.
    At most `max_concurrent` jobs run at a time; extra jobs wait in order.
    """

    def __init__(self, max_concurrent: int) -> None:
        self.max_concurrent = max(1, int(max_concurrent))
        self._queue: asyncio.Queue[tuple[Judge0Job, asyncio.Future[Any]]] = asyncio.Queue()
        self._workers_started = False
        self._startup_lock = asyncio.Lock()
        self._workers: list[asyncio.Task[Any]] = []
        self._active = 0
        self._active_lock = asyncio.Lock()

    async def _ensure_workers(self) -> None:
        if self._workers_started:
            return
        async with self._startup_lock:
            if self._workers_started:
                return
            for _ in range(self.max_concurrent):
                self._workers.append(asyncio.create_task(self._worker_loop()))
            self._workers_started = True

    async def _worker_loop(self) -> None:
        while True:
            job_factory, future = await self._queue.get()
            try:
                async with self._active_lock:
                    self._active += 1
                if future.cancelled():
                    continue
                result = await job_factory()
                if not future.cancelled():
                    future.set_result(result)
            except Exception as exc:
                if not future.cancelled():
                    future.set_exception(exc)
            finally:
                async with self._active_lock:
                    self._active = max(0, self._active - 1)
                self._queue.task_done()

    async def run(self, job_factory: Judge0Job) -> Any:
        await self._ensure_workers()
        loop = asyncio.get_running_loop()
        result_future: asyncio.Future[Any] = loop.create_future()
        await self._queue.put((job_factory, result_future))
        return await result_future

    async def stats(self) -> dict[str, int]:
        async with self._active_lock:
            active = self._active
        return {
            "max_concurrent": self.max_concurrent,
            "active": active,
            "queued": self._queue.qsize(),
        }


judge0_execution_queue = Judge0ExecutionQueue(
    max_concurrent=int(os.getenv("JUDGE0_MAX_CONCURRENT_EXECUTIONS", "12"))
)
