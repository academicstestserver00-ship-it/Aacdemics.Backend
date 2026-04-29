

# """
# Database Models
# SQLAlchemy ORM models for all tables
# """

# from sqlalchemy import Column, Integer, String, Text, Boolean, Float, DateTime, ForeignKey, Enum as SQLEnum
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func
# from app.database import Base
# import enum


# class UserRole(str, enum.Enum):
#     TEACHER = "teacher"
#     STUDENT = "student"


# class Difficulty(str, enum.Enum):
#     EASY = "easy"
#     MEDIUM = "medium"
#     HARD = "hard"


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String(255), unique=True, nullable=False, index=True)
#     password_hash = Column(String(255), nullable=False)
#     role = Column(SQLEnum(UserRole), nullable=False)
#     name = Column(String(255), nullable=False)
#     created_at = Column(DateTime(timezone=True), server_default=func.now())

#     created_tests = relationship("Test", back_populates="teacher", foreign_keys="Test.teacher_id")
#     submissions = relationship("Submission", back_populates="student")


# class Test(Base):
#     __tablename__ = "tests"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(255), nullable=False)
#     description = Column(Text)
#     teacher_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     duration_minutes = Column(Integer, default=60)
#     is_active = Column(Boolean, default=True)
#     # ✅ NEW: comma-separated list e.g. "python,c,cpp,java"
#     allowed_languages = Column(String(100), nullable=False, default="python,c,cpp,java")
#     created_at = Column(DateTime(timezone=True), server_default=func.now())

#     teacher = relationship("User", back_populates="created_tests", foreign_keys=[teacher_id])
#     questions = relationship("Question", back_populates="test", cascade="all, delete-orphan")


# class Question(Base):
#     __tablename__ = "questions"

#     id = Column(Integer, primary_key=True, index=True)
#     test_id = Column(Integer, ForeignKey("tests.id"), nullable=False)
#     title = Column(String(255), nullable=False)
#     description = Column(Text, nullable=False)
#     difficulty = Column(SQLEnum(Difficulty), default=Difficulty.MEDIUM)
#     topic = Column(String(100), nullable=False, default="GENERAL")
#     points = Column(Integer, default=10)
#     time_limit_ms = Column(Integer, default=2000)
#     created_at = Column(DateTime(timezone=True), server_default=func.now())

#     test = relationship("Test", back_populates="questions")
#     test_cases = relationship("TestCase", back_populates="question", cascade="all, delete-orphan")
#     submissions = relationship("Submission", back_populates="question")


# class TestCase(Base):
#     __tablename__ = "test_cases"

#     id = Column(Integer, primary_key=True, index=True)
#     question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
#     input = Column(Text, nullable=False)
#     expected_output = Column(Text, nullable=False)
#     is_hidden = Column(Boolean, default=False)
#     points = Column(Integer, default=1)
#     created_at = Column(DateTime(timezone=True), server_default=func.now())

#     question = relationship("Question", back_populates="test_cases")


# class Submission(Base):
#     __tablename__ = "submissions"

#     id = Column(Integer, primary_key=True, index=True)
#     student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
#     code = Column(Text, nullable=False)
#     language = Column(String(20), nullable=False)
#     score = Column(Float, default=0.0)
#     verdict = Column(String(50))
#     execution_time_ms = Column(Integer)
#     passed_tests = Column(Integer, default=0)
#     total_tests = Column(Integer, default=0)
#     tab_switches = Column(Integer, default=0)
#     paste_count = Column(Integer, default=0)
#     submitted_at = Column(DateTime(timezone=True), server_default=func.now())

#     student = relationship("User", back_populates="submissions")
#     question = relationship("Question", back_populates="submissions")



"""
db_models.py
SQLAlchemy models are no longer used — migrated to Firebase Realtime Database.
This file is kept as an empty stub to avoid import errors during transition.
"""

from sqlalchemy import Column, Integer, String, Text, Boolean, Float, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum


class UserRole(str, enum.Enum):
    TEACHER = "teacher"
    STUDENT = "student"


class Difficulty(str, enum.Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(SQLEnum(UserRole), nullable=False)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    created_tests = relationship("Test", back_populates="teacher", foreign_keys="Test.teacher_id")
    submissions = relationship("Submission", back_populates="student")


class Test(Base):
    __tablename__ = "tests"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    teacher_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    duration_minutes = Column(Integer, default=60)
    is_active = Column(Boolean, default=True)
    allowed_languages = Column(String(100), nullable=False, default="python,c,cpp,java")
    # ✅ NEW FIELDS
    start_date = Column(DateTime(timezone=True), nullable=True)
    end_date = Column(DateTime(timezone=True), nullable=True)
    test_type = Column(String(20), nullable=False, default="invite_only")
    tags = Column(String(255), nullable=False, default="")
    assessment_id = Column(String(20), nullable=False, default="")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    teacher = relationship("User", back_populates="created_tests", foreign_keys=[teacher_id])
    questions = relationship("Question", back_populates="test", cascade="all, delete-orphan")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    test_id = Column(Integer, ForeignKey("tests.id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    difficulty = Column(SQLEnum(Difficulty), default=Difficulty.MEDIUM)
    topic = Column(String(100), nullable=False, default="GENERAL")
    points = Column(Integer, default=10)
    time_limit_ms = Column(Integer, default=2000)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    test = relationship("Test", back_populates="questions")
    test_cases = relationship("TestCase", back_populates="question", cascade="all, delete-orphan")
    submissions = relationship("Submission", back_populates="question")


class TestCase(Base):
    __tablename__ = "test_cases"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    input = Column(Text, nullable=False)
    expected_output = Column(Text, nullable=False)
    is_hidden = Column(Boolean, default=False)
    points = Column(Integer, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    question = relationship("Question", back_populates="test_cases")


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    code = Column(Text, nullable=False)
    language = Column(String(20), nullable=False)
    score = Column(Float, default=0.0)
    verdict = Column(String(50))
    execution_time_ms = Column(Integer)
    passed_tests = Column(Integer, default=0)
    total_tests = Column(Integer, default=0)
    tab_switches = Column(Integer, default=0)
    paste_count = Column(Integer, default=0)
    submitted_at = Column(DateTime(timezone=True), server_default=func.now())

    student = relationship("User", back_populates="submissions")
    question = relationship("Question", back_populates="submissions")