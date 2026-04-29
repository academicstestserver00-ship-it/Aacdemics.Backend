"""
Base Runner
Abstract class that all language runners inherit from
"""

from abc import ABC, abstractmethod
from typing import Tuple
from app.models.test_case import TestResult, Verdict


class BaseRunner(ABC):
    """
    Abstract base class for code execution runners
    """
    
    def __init__(self, time_limit_ms: int = 2000, memory_limit_mb: int = 256):
        self.time_limit_ms = time_limit_ms
        self.memory_limit_mb = memory_limit_mb
    
    @abstractmethod
    async def execute(self, code: str, test_input: str) -> TestResult:
        """
        Execute code with given input and return result
        
        Args:
            code: Source code to execute
            test_input: Input to pass via stdin
            
        Returns:
            TestResult with verdict, output, and execution time
        """
        pass
    
    @abstractmethod
    def get_language_name(self) -> str:
        """Return the language name (e.g., 'python', 'c', 'java')"""
        pass
    
    def compare_output(self, actual: str, expected: str) -> bool:
        """
        Compare actual output with expected output
        Default implementation: strip whitespace and compare
        
        Args:
            actual: Program's actual output
            expected: Expected output
            
        Returns:
            True if outputs match, False otherwise
        """
        # Strip trailing whitespace from each line and compare
        actual_lines = [line.rstrip() for line in actual.splitlines()]
        expected_lines = [line.rstrip() for line in expected.splitlines()]
        
        return actual_lines == expected_lines