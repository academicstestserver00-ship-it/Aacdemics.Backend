"""
C Runner
Compiles and executes C code in a controlled environment
"""

import asyncio
import tempfile
import os
import time
import subprocess
from pathlib import Path
from app.runners.base import BaseRunner
from app.models.test_case import TestResult, Verdict
from app.config import settings


class CRunner(BaseRunner):
    """
    Compiles and executes C code with input and captures output
    """
    
    def get_language_name(self) -> str:
        return "c"
    
    def _run_sync(self, code: str, test_input: str, timeout_seconds: float) -> dict:
        """
        Synchronous compilation and execution helper
        """
        temp_dir = None
        source_file = None
        executable_file = None
        
        try:
            # Create temp directory
            temp_dir = tempfile.mkdtemp(dir=settings.TEMP_CODE_DIR)
            
            # Write source code
            source_file = os.path.join(temp_dir, "solution.c")
            with open(source_file, 'w', encoding='utf-8') as f:
                f.write(code)
            
            # Determine executable name (Windows vs Unix)
            if os.name == 'nt':  # Windows
                executable_file = os.path.join(temp_dir, "solution.exe")
            else:  # Linux/Mac
                executable_file = os.path.join(temp_dir, "solution")
            
            # Compile the C code
            compile_result = subprocess.run(
                ['gcc', source_file, '-o', executable_file, '-lm'],  # -lm for math library
                capture_output=True,
                text=True,
                timeout=10,  # Compilation timeout
                encoding='utf-8',
                errors='replace'
            )
            
            # Check compilation errors
            if compile_result.returncode != 0:
                return {
                    'compilation_error': True,
                    'stderr': compile_result.stderr,
                    'stdout': compile_result.stdout
                }
            
            # Execute the compiled binary
            exec_result = subprocess.run(
                [executable_file],
                input=test_input,
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
                encoding='utf-8',
                errors='replace'
            )
            
            return {
                'returncode': exec_result.returncode,
                'stdout': exec_result.stdout,
                'stderr': exec_result.stderr,
                'timed_out': False
            }
            
        except subprocess.TimeoutExpired:
            return {
                'returncode': -1,
                'stdout': '',
                'stderr': '',
                'timed_out': True
            }
        except FileNotFoundError as e:
            if 'gcc' in str(e):
                return {
                    'returncode': -1,
                    'stdout': '',
                    'stderr': '',
                    'error': 'GCC compiler not found. Please install GCC to run C code.'
                }
            return {
                'returncode': -1,
                'stdout': '',
                'stderr': '',
                'error': str(e)
            }
        except Exception as e:
            return {
                'returncode': -1,
                'stdout': '',
                'stderr': '',
                'error': str(e)
            }
        finally:
            # Clean up temp files
            try:
                if source_file and os.path.exists(source_file):
                    os.unlink(source_file)
                if executable_file and os.path.exists(executable_file):
                    os.unlink(executable_file)
                if temp_dir and os.path.exists(temp_dir):
                    os.rmdir(temp_dir)
            except:
                pass
    
    async def execute(self, code: str, test_input: str) -> TestResult:
        """
        Compile and execute C code with given input
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
            
            # Handle compilation error
            if result.get('compilation_error'):
                return TestResult(
                    id="",
                    verdict=Verdict.COMPILATION_ERROR,
                    stdout=result.get('stdout', ''),
                    stderr=result.get('stderr', ''),
                    time_ms=execution_time_ms,
                    error_message="Compilation failed"
                )
            
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


def create_c_runner(time_limit_ms: int = 2000) -> CRunner:
    """
    Create a C runner instance
    """
    return CRunner(time_limit_ms=time_limit_ms)