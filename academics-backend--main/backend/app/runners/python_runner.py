# """
# Python Runner
# Executes Python code in a controlled environment
# """

# import asyncio
# import tempfile
# import os
# import time
# from pathlib import Path
# from app.runners.base import BaseRunner
# from app.models.test_case import TestResult, Verdict
# from app.config import settings


# class PythonRunner(BaseRunner):
#     """
#     Executes Python code with input and captures output
#     """
    
#     def get_language_name(self) -> str:
#         return "python"
    
#     async def execute(self, code: str, test_input: str) -> TestResult:
#         """
#         Execute Python code with given input
        
#         Args:
#             code: Python source code
#             test_input: Input to pass via stdin
            
#         Returns:
#             TestResult with execution details
#         """
#         start_time = time.time()
        
#         # Create temporary file for code
#         temp_file = None
#         try:
#             # Create temp directory if not exists
#             os.makedirs(settings.TEMP_CODE_DIR, exist_ok=True)
            
#             # Write code to temporary file
#             with tempfile.NamedTemporaryFile(
#                 mode='w',
#                 suffix='.py',
#                 dir=settings.TEMP_CODE_DIR,
#                 delete=False,
#                 encoding='utf-8'
#             ) as f:
#                 f.write(code)
#                 temp_file = f.name
            
#             # Execute the code
#             process = await asyncio.create_subprocess_exec(
#                 'python', temp_file,
#                 stdin=asyncio.subprocess.PIPE,
#                 stdout=asyncio.subprocess.PIPE,
#                 stderr=asyncio.subprocess.PIPE
#             )
            
#             # Set timeout
#             timeout_seconds = self.time_limit_ms / 1000.0
            
#             try:
#                 stdout, stderr = await asyncio.wait_for(
#                     process.communicate(input=test_input.encode('utf-8')),
#                     timeout=timeout_seconds
#                 )
                
#                 execution_time_ms = int((time.time() - start_time) * 1000)
                
#                 # Decode output
#                 stdout_str = stdout.decode('utf-8', errors='replace')
#                 stderr_str = stderr.decode('utf-8', errors='replace')
                
#                 # Check for runtime errors
#                 if process.returncode != 0:
#                     return TestResult(
#                         id="",
#                         verdict=Verdict.RUNTIME_ERROR,
#                         stdout=stdout_str,
#                         stderr=stderr_str,
#                         time_ms=execution_time_ms,
#                         error_message=f"Process exited with code {process.returncode}"
#                     )
                
#                 # Success - return output
#                 return TestResult(
#                     id="",
#                     verdict=Verdict.PASS,
#                     stdout=stdout_str,
#                     stderr=stderr_str,
#                     time_ms=execution_time_ms
#                 )
                
#             except asyncio.TimeoutError:
#                 # Kill the process
#                 try:
#                     process.kill()
#                     await process.wait()
#                 except:
#                     pass
                
#                 execution_time_ms = int((time.time() - start_time) * 1000)
                
#                 return TestResult(
#                     id="",
#                     verdict=Verdict.TIME_LIMIT_EXCEEDED,
#                     stdout="",
#                     stderr="",
#                     time_ms=execution_time_ms,
#                     error_message=f"Execution exceeded {self.time_limit_ms}ms time limit"
#                 )
        
#         except Exception as e:
#             execution_time_ms = int((time.time() - start_time) * 1000)
            
#             return TestResult(
#                 id="",
#                 verdict=Verdict.UNKNOWN_ERROR,
#                 stdout="",
#                 stderr="",
#                 time_ms=execution_time_ms,
#                 error_message=f"Execution failed: {str(e)}"
#             )
        
#         finally:
#             # Clean up temporary file
#             if temp_file and os.path.exists(temp_file):
#                 try:
#                     os.unlink(temp_file)
#                 except:
#                     pass


# def create_python_runner(time_limit_ms: int = 2000) -> PythonRunner:
#     """
#     Create a Python runner instance
    
#     Args:
#         time_limit_ms: Time limit in milliseconds
        
#     Returns:
#         PythonRunner instance
#     """
#     return PythonRunner(time_limit_ms=time_limit_ms)


"""
Python Runner
Executes Python code in a controlled environment
Windows-compatible version using subprocess.run
"""

import asyncio
import tempfile
import os
import time
import subprocess
from app.runners.base import BaseRunner
from app.models.test_case import TestResult, Verdict
from app.config import settings


class PythonRunner(BaseRunner):
    """
    Executes Python code with input and captures output
    """
    
    def get_language_name(self) -> str:
        return "python"
    
    def _run_sync(self, code: str, test_input: str, timeout_seconds: float) -> dict:
        """
        Synchronous execution helper (runs in thread)
        """
        temp_file = None
        
        try:
            # Create temp directory if not exists
            os.makedirs(settings.TEMP_CODE_DIR, exist_ok=True)
            
            # Write code to temporary file
            with tempfile.NamedTemporaryFile(
                mode='w',
                suffix='.py',
                dir=settings.TEMP_CODE_DIR,
                delete=False,
                encoding='utf-8'
            ) as f:
                f.write(code)
                temp_file = f.name
            
            # Execute using subprocess.run
            result = subprocess.run(
                ['python', temp_file],
                input=test_input,
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
                encoding='utf-8',
                errors='replace'
            )
            
            return {
                'returncode': result.returncode,
                'stdout': result.stdout,
                'stderr': result.stderr,
                'timed_out': False
            }
            
        except subprocess.TimeoutExpired:
            return {
                'returncode': -1,
                'stdout': '',
                'stderr': '',
                'timed_out': True
            }
        except Exception as e:
            return {
                'returncode': -1,
                'stdout': '',
                'stderr': '',
                'error': str(e)
            }
        finally:
            # Clean up temporary file
            if temp_file and os.path.exists(temp_file):
                try:
                    os.unlink(temp_file)
                except:
                    pass
    
    async def execute(self, code: str, test_input: str) -> TestResult:
        """
        Execute Python code with given input
        """
        start_time = time.time()
        
        try:
            # Set timeout
            timeout_seconds = self.time_limit_ms / 1000.0
            
            # Run in thread to avoid blocking
            result = await asyncio.to_thread(
                self._run_sync,
                code,
                test_input,
                timeout_seconds
            )
            
            execution_time_ms = int((time.time() - start_time) * 1000)
            
            # Handle timeout
            if result.get('timed_out'):
                return TestResult(
                    id="",
                    verdict=Verdict.TIME_LIMIT_EXCEEDED,
                    stdout="",
                    stderr="",
                    time_ms=execution_time_ms,
                    error_message=f"Execution exceeded {self.time_limit_ms}ms time limit"
                )
            
            # Handle other errors
            if 'error' in result:
                return TestResult(
                    id="",
                    verdict=Verdict.UNKNOWN_ERROR,
                    stdout="",
                    stderr="",
                    time_ms=execution_time_ms,
                    error_message=f"Execution error: {result['error']}"
                )
            
            # Handle runtime errors
            if result['returncode'] != 0:
                return TestResult(
                    id="",
                    verdict=Verdict.RUNTIME_ERROR,
                    stdout=result['stdout'],
                    stderr=result['stderr'],
                    time_ms=execution_time_ms,
                    error_message=f"Process exited with code {result['returncode']}"
                )
            
            # Success
            return TestResult(
                id="",
                verdict=Verdict.PASS,
                stdout=result['stdout'],
                stderr=result['stderr'],
                time_ms=execution_time_ms
            )
        
        except Exception as e:
            execution_time_ms = int((time.time() - start_time) * 1000)
            
            return TestResult(
                id="",
                verdict=Verdict.UNKNOWN_ERROR,
                stdout="",
                stderr="",
                time_ms=execution_time_ms,
                error_message=f"Execution failed: {str(e)}"
            )


def create_python_runner(time_limit_ms: int = 2000) -> PythonRunner:
    """
    Create a Python runner instance
    """
    return PythonRunner(time_limit_ms=time_limit_ms)