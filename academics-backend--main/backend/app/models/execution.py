"""
Execution Models
Defines request and response structures for code execution API
"""

from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from app.models.test_case import TestCase, TestResult, Verdict


class ExecutionRequest(BaseModel):
    """
    Request model for code execution endpoint
    """
    language: str = Field(..., description="Programming language (python, c, cpp, java)")
    code: str = Field(..., description="Source code to execute", min_length=1)
    tests: List[TestCase] = Field(..., description="List of test cases to run", min_items=1)
    time_limit_ms: int = Field(default=2000, description="Time limit per test in milliseconds", ge=100, le=10000)
    
    @field_validator('language')
    @classmethod
    def validate_language(cls, v):
        allowed = ['python', 'c', 'cpp', 'java']
        if v.lower() not in allowed:
            raise ValueError(f"Language must be one of {allowed}")
        return v.lower()
    
    @field_validator('code')
    @classmethod
    def validate_code(cls, v):
        if len(v.strip()) == 0:
            raise ValueError("Code cannot be empty")
        return v


class ExecutionSummary(BaseModel):
    """
    Summary of test execution results
    """
    total: int = Field(..., description="Total number of test cases")
    passed: int = Field(..., description="Number of passed test cases")
    failed: int = Field(..., description="Number of failed test cases")
    errors: int = Field(default=0, description="Number of test cases with errors")
    score: float = Field(default=0.0, description="Score as percentage (0-100)")
    total_time_ms: int = Field(default=0, description="Total execution time")


class ExecutionResponse(BaseModel):
    """
    Response model for code execution endpoint
    """
    status: str = Field(..., description="Overall status (OK, ERROR)")
    summary: ExecutionSummary = Field(..., description="Execution summary")
    results: List[TestResult] = Field(..., description="Individual test case results")
    compilation_error: Optional[str] = Field(default=None, description="Compilation error if any")
