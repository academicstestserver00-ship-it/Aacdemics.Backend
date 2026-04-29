"""
Java Runner
Compiles and executes Java code in a controlled environment
"""

import asyncio
import tempfile
import os
import time
import subprocess
import re
from pathlib import Path
from app.runners.base import BaseRunner
from app.models.test_case import TestResult, Verdict
from app.config import settings


class JavaRunner(BaseRunner):
    """
    Compiles and executes Java code with input and captures output
    """
    
    def get_language_name(self) -> str:
        return "java"
    
    def _extract_class_name(self, code: str) -> str:
        """
        Extract the public class name from Java code
        Returns 'Main' as default if not found
        """
        # Look for: public class ClassName
        match = re.search(r'public\s+class\s+(\w+)', code)
        if match:
            return match.group(1)
        
        # Look for: class ClassName (non-public)
        match = re.search(r'class\s+(\w+)', code)
        if match:
            return match.group(1)
        
        # Default
        return 'Main'
    
    def _run_sync(self, code: str, test_input: str, timeout_seconds: float) -> dict:
        """
        Synchronous compilation and execution helper
        """
        temp_dir = None
        source_file = None
        
        try:
            # Create temp directory
            temp_dir = tempfile.mkdtemp(dir=settings.TEMP_CODE_DIR)
            
            # Extract class name from code
            class_name = self._extract_class_name(code)
            
            # Write source code with correct filename
            source_file = os.path.join(temp_dir, f"{class_name}.java")
            with open(source_file, 'w', encoding='utf-8') as f:
                f.write(code)
            
            # Compile the Java code
            compile_result = subprocess.run(
                ['javac', source_file],
                capture_output=True,
                text=True,
                timeout=10,  # Compilation timeout
                encoding='utf-8',
                errors='replace',
                cwd=temp_dir
            )
            
            # Check compilation errors
            if compile_result.returncode != 0:
                return {
                    'compilation_error': True,
                    'stderr': compile_result.stderr,
                    'stdout': compile_result.stdout
                }
            
            # Execute the compiled Java class
            exec_result = subprocess.run(
                ['java', class_name],
                input=test_input,
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
                encoding='utf-8',
                errors='replace',
                cwd=temp_dir  # Run in temp directory where .class file is
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
            if 'javac' in str(e) or 'java' in str(e):
                return {
                    'returncode': -1,
                    'stdout': '',
                    'stderr': '',
                    'error': 'Java compiler (JDK) not found. Please install JDK to run Java code.'
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
                if temp_dir and os.path.exists(temp_dir):
                    # Remove all files in temp directory
                    for file in os.listdir(temp_dir):
                        file_path = os.path.join(temp_dir, file)
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                    os.rmdir(temp_dir)
            except:
                pass
    
    async def execute(self, code: str, test_input: str) -> TestResult:
        """
        Compile and execute Java code with given input
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


def create_java_runner(time_limit_ms: int = 2000) -> JavaRunner:
    """
    Create a Java runner instance
    """
    return JavaRunner(time_limit_ms=time_limit_ms)