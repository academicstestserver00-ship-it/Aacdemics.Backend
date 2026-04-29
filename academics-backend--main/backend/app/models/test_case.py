"""
Test Case Models
Defines the structure for test cases and execution verdicts
"""

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class Verdict(str, Enum):
    """
    Possible verdicts for a test case execution
    """
    PASS = "PASS"
    FAIL = "FAIL"
    RUNTIME_ERROR = "RUNTIME_ERROR"
    TIME_LIMIT_EXCEEDED = "TIME_LIMIT_EXCEEDED"
    MEMORY_LIMIT_EXCEEDED = "MEMORY_LIMIT_EXCEEDED"
    COMPILATION_ERROR = "COMPILATION_ERROR"
    UNKNOWN_ERROR = "UNKNOWN_ERROR"


class TestCase(BaseModel):
    """
    Represents a single test case for code execution
    """
    id: str = Field(..., description="Unique identifier for this test case")
    input: str = Field(..., description="Input data to pass to the program via stdin")
    expected_output: str = Field(..., description="Expected output from the program")
    is_hidden: bool = Field(default=False, description="Whether this is a hidden test case")
    points: int = Field(default=1, description="Points awarded for passing this test")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "tc1",
                "input": "5\n",
                "expected_output": "120\n",
                "is_hidden": False,
                "points": 10
            }
        }


class TestResult(BaseModel):
    """
    Result of executing a single test case
    """
    id: str = Field(..., description="Test case ID")
    verdict: Verdict = Field(..., description="Execution verdict")
    stdout: str = Field(default="", description="Program's standard output")
    stderr: str = Field(default="", description="Program's standard error")
    time_ms: int = Field(default=0, description="Execution time in milliseconds")
    memory_kb: Optional[int] = Field(default=None, description="Memory used in KB")
    error_message: Optional[str] = Field(default=None, description="Error details if any")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "tc1",
                "verdict": "PASS",
                "stdout": "120\n",
                "stderr": "",
                "time_ms": 45,
                "memory_kb": 8192,
                "error_message": None
            }
        }