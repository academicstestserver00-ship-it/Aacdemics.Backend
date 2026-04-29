from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Union, List
import asyncio
import base64
import httpx
import math
import os
import time

from app.utils.judge0_queue import judge0_execution_queue

router = APIRouter()

JUDGE0_URL = os.getenv("JUDGE0_URL", "https://ce.judge0.com")
JUDGE0_AUTH_TOKEN = os.getenv("JUDGE0_AUTH_TOKEN", "")
JUDGE0_TIMEOUT_SECONDS = float(os.getenv("JUDGE0_TIMEOUT_SECONDS", "15"))
JUDGE0_BASE64 = os.getenv("JUDGE0_BASE64_ENCODED", "true").lower() == "true"
MAX_TIME_LIMIT_SECONDS = float(os.getenv("MAX_TIME_LIMIT_SECONDS", "5"))
MAX_WALL_TIME_LIMIT_SECONDS = float(os.getenv("MAX_WALL_TIME_LIMIT_SECONDS", "10"))
MAX_OUTPUT_KB = int(os.getenv("MAX_OUTPUT_KB", "64"))

HEADERS = {
    "Content-Type": "application/json",
}

if JUDGE0_AUTH_TOKEN:
    HEADERS["X-Auth-Token"] = JUDGE0_AUTH_TOKEN

LANGUAGE_IDS = {
    "python": 71,
    "c": 50,
    "cpp": 54,
    "java": 62,
}

LANGUAGE_ALIASES = {
    "py": "python",
    "python3": "python",
    "c++": "cpp",
    "cxx": "cpp",
}


class TestCase(BaseModel):
    id: Union[str, int]
    input: str
    expected_output: str
    is_hidden: Optional[bool] = False
    points: Optional[int] = 1


class ExecuteRequest(BaseModel):
    code: str
    language: str
    test_cases: List[TestCase]
    question_id: Optional[Union[str, int]] = None
    time_limit: Optional[float] = 5.0
    memory_limit: Optional[int] = 256000


def normalize(text: str) -> str:
    return text.strip()


def maybe_b64(value: str) -> str:
    if not JUDGE0_BASE64:
        return value
    raw = value if value is not None else ""
    return base64.b64encode(raw.encode("utf-8", errors="replace")).decode("ascii")


def maybe_b64_decode(value: str) -> str:
    if not JUDGE0_BASE64:
        return value
    if value is None:
        return ""
    try:
        return base64.b64decode(value).decode("utf-8", errors="replace")
    except Exception:
        return value


def get_language_id(language: str) -> int:
    raw = language.lower().strip()
    lang = LANGUAGE_ALIASES.get(raw, raw)
    if lang not in LANGUAGE_IDS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported language '{language}'. Supported: {list(LANGUAGE_IDS.keys())}",
        )
    return LANGUAGE_IDS[lang]


async def submit_token(
    client: httpx.AsyncClient,
    code: str,
    language_id: int,
    stdin: str,
    time_limit: float,
    memory_limit: int,
) -> tuple[str, float]:
    safe_time_limit = max(0.5, min(float(time_limit or 0), MAX_TIME_LIMIT_SECONDS))
    safe_wall_limit = max(1.0, min(float(safe_time_limit * 2), MAX_WALL_TIME_LIMIT_SECONDS))
    payload = {
        "source_code": maybe_b64(code),
        "language_id": language_id,
        "stdin": maybe_b64(stdin),
        "cpu_time_limit": safe_time_limit,
        "wall_time_limit": safe_wall_limit,
        "memory_limit": memory_limit,
        "enable_per_process_and_thread_time_limit": True,
        "max_output_size": MAX_OUTPUT_KB,
    }
    submitted_at = time.monotonic()
    resp = await client.post(
        f"{JUDGE0_URL}/submissions?base64_encoded={'true' if JUDGE0_BASE64 else 'false'}&wait=false",
        json=payload,
        headers=HEADERS,
    )
    if resp.status_code not in (200, 201):
        raise HTTPException(
            status_code=502,
            detail=f"Judge0 submission failed: {resp.status_code} {resp.text}",
        )
    token = resp.json().get("token")
    if not token:
        raise HTTPException(status_code=502, detail="Judge0 did not return a submission token")
    return token, submitted_at


async def poll_token(
    client: httpx.AsyncClient,
    token: str,
    max_wait_seconds: int = 30,
    poll_interval: float = 0.6,
) -> tuple[dict, float]:
    start = time.monotonic()
    last_error = None
    while time.monotonic() - start < max_wait_seconds:
        await asyncio.sleep(poll_interval)
        try:
            resp = await client.get(
                f"{JUDGE0_URL}/submissions/{token}?base64_encoded={'true' if JUDGE0_BASE64 else 'false'}",
                headers=HEADERS,
            )
        except Exception as e:
            last_error = str(e)
            continue
        if resp.status_code != 200:
            try:
                body = resp.text.strip()
            except Exception:
                body = ""
            if body:
                last_error = f"HTTP {resp.status_code} {body}"
            else:
                last_error = f"HTTP {resp.status_code}"
            continue
        result = resp.json()
        status_id = result.get("status", {}).get("id", 0)
        if status_id not in (1, 2):
            return result, time.monotonic()

    status_desc = "Judge0 Timeout"
    if last_error and (not last_error.startswith("HTTP 4")) and (not last_error.startswith("HTTP 5")):
        status_desc = "Execution Service Error"
    elif last_error and last_error.startswith("HTTP"):
        status_desc = "Execution Service Error"

    return {
        "status": {"id": 20 if status_desc == "Execution Service Error" else 13, "description": status_desc},
        "stdout": "",
        "stderr": last_error or "Execution service timed out while polling Judge0.",
        "compile_output": "",
        "time": str(max_wait_seconds),
        "memory": None,
    }, time.monotonic()


def parse_result(judge0_result: dict, test_case: TestCase) -> dict:
    status = judge0_result.get("status", {})
    status_id = status.get("id", 0)
    status_desc = status.get("description", "Unknown")

    stdout = maybe_b64_decode(judge0_result.get("stdout") or "")
    stderr = maybe_b64_decode(judge0_result.get("stderr") or "")
    compile_output = maybe_b64_decode(judge0_result.get("compile_output") or "")
    time_ms = float(judge0_result.get("time") or 0) * 1000
    memory_kb = float(judge0_result.get("memory") or 0)

    error = None
    if compile_output.strip():
        status_id = 6
        status_desc = "Compilation Error"
        error = compile_output or "Compilation error"
    elif status_id == 6:
        error = compile_output or "Compilation error"
    elif status_id == 5:
        error = "Time Limit Exceeded"
    elif status_id == 13 or status_desc == "Judge0 Timeout":
        error = f"Execution Service Timeout: {stderr or status_desc}"
    elif status_id == 20 or status_desc == "Execution Service Error":
        error = f"Execution Service Error: {stderr or status_desc}"
    elif status_id == 11:
        error = f"Runtime Error: {stderr or status_desc}"
    elif status_id in (12, 14, 15):
        error = f"Runtime Error: {stderr or status_desc}"
    elif status_id not in (3,):
        error = stderr or compile_output or status_desc

    actual = normalize(stdout)
    expected = normalize(test_case.expected_output)
    passed = (status_id == 3) and (actual == expected)

    if status_id == 5:
        verdict = "TIME_LIMIT_EXCEEDED"
    elif passed:
        verdict = "PASS"
    else:
        verdict = "FAIL"

    return {
        "id": test_case.id,
        "verdict": verdict,
        "passed": passed,
        "actual_output": actual,
        "expected_output": expected,
        "is_hidden": test_case.is_hidden,
        "points_earned": test_case.points if passed else 0,
        "error": error,
        "stdout": actual,
        "stderr": stderr or compile_output or None,
        "time_ms": round(time_ms, 2),
        "memory_kb": round(memory_kb, 2),
        "status": status_desc,
    }


@router.post("/api/execute")
async def execute_code(request: ExecuteRequest):
    if not request.test_cases:
        raise HTTPException(status_code=400, detail="No test cases provided")

    language_id = get_language_id(request.language)
    timeout = httpx.Timeout(JUDGE0_TIMEOUT_SECONDS)

    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            poll_timeout = min(max(6, int(request.time_limit * 2 + 4)), 20)

            async def _execute_single_case(tc: TestCase):
                token, submitted_at = await submit_token(
                    client,
                    request.code,
                    language_id,
                    tc.input,
                    request.time_limit,
                    request.memory_limit,
                )
                judge0_result, finished_at = await poll_token(client, token, poll_timeout, 0.6)
                return (token, submitted_at), (judge0_result, finished_at)

            async def _run_judge0():
                case_tasks = [
                    judge0_execution_queue.run(lambda tc=tc: _execute_single_case(tc))
                    for tc in request.test_cases
                ]
                case_results = await asyncio.gather(*case_tasks)
                tokens = [token_info for token_info, _ in case_results]
                judge0_results = [result_info for _, result_info in case_results]
                return tokens, judge0_results

            queue_waves = max(
                1,
                math.ceil(len(request.test_cases) / max(1, judge0_execution_queue.max_concurrent)),
            )
            overall_timeout = min(max(8, queue_waves * (poll_timeout + 4)), 180)
            tokens, judge0_results = await asyncio.wait_for(_run_judge0(), timeout=overall_timeout)
        except asyncio.TimeoutError:
            raise HTTPException(
                status_code=504,
                detail="Execution timed out. Please try again or reduce input size.",
            )

    results = []
    total_passed = 0
    total_score = 0.0
    max_score = sum(tc.points for tc in request.test_cases)
    compilation_error = None
    compiled_langs = {"c", "cpp", "java"}
    compile_time_ms = None
    durations_ms = []

    for (token, submitted_at), (judge0_result, finished_at) in zip(tokens, judge0_results):
        try:
            durations_ms.append((finished_at - submitted_at) * 1000.0)
        except Exception:
            pass

    if request.language.lower().strip() in compiled_langs and durations_ms:
        compile_time_ms = int(round(min(durations_ms)))

    for tc, (judge0_result, _finished_at) in zip(request.test_cases, judge0_results):
        try:
            result = parse_result(judge0_result, tc)
            if result.get("status") == "Compilation Error" and not compilation_error:
                compilation_error = result.get("stderr") or result.get("error")
        except Exception as e:
            result = {
                "id": tc.id,
                "verdict": "FAIL",
                "passed": False,
                "actual_output": "",
                "expected_output": normalize(tc.expected_output),
                "is_hidden": tc.is_hidden,
                "points_earned": 0,
                "error": f"Parse error: {str(e)}",
                "stdout": None,
                "stderr": str(e),
                "time_ms": None,
                "memory_kb": None,
                "status": "Internal Error",
            }

        results.append(result)
        if result["passed"]:
            total_passed += 1
            total_score += result["points_earned"]

    score = round((total_score / max_score * 100) if max_score > 0 else 0, 1)

    return {
        "results": results,
        "total_passed": total_passed,
        "total_cases": len(request.test_cases),
        "total_score": total_score,
        "max_score": max_score,
        "success": total_passed == len(request.test_cases),
        "compilation_error": compilation_error,
        "compilation_time_ms": compile_time_ms,
        "summary": {
            "score": score,
            "passed": total_passed,
            "total": len(request.test_cases),
        },
    }


@router.get("/api/execute/health")
async def execution_health():
    queue_stats = await judge0_execution_queue.stats()
    try:
        timeout = httpx.Timeout(5.0)
        async with httpx.AsyncClient(timeout=timeout) as client:
            resp = await client.get(
                f"{JUDGE0_URL}/system_info",
                headers=HEADERS,
            )
        if resp.status_code == 200:
            return {"status": "ok", "judge0": "reachable", "queue": queue_stats}
        return {"status": "degraded", "judge0": f"HTTP {resp.status_code}", "queue": queue_stats}
    except Exception as e:
        return {"status": "error", "judge0": str(e), "queue": queue_stats}
