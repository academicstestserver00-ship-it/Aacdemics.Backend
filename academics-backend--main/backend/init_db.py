"""
Database Initialization Script
Creates all tables in the database
Run this once to set up the database schema
"""

import sys
from pathlib import Path

# Add the backend directory to Python path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

from app.database import engine, Base
from app.models.db_models import User, Test, Question, TestCase, Submission

def init_database():
    """
    Create all tables in the database
    """
    print("=" * 60)
    print("Initializing Database...")
    print("=" * 60)
    
    try:
        # Create all tables
        print("\nCreating tables...")
        Base.metadata.create_all(bind=engine)
        
        print("\n✅ Database tables created successfully!")
        print("\nTables created:")
        print("  - users")
        print("  - tests")
        print("  - questions")
        print("  - test_cases")
        print("  - submissions")
        print("\n" + "=" * 60)
        print("Database initialization complete!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Error creating tables: {e}")
        sys.exit(1)


if __name__ == "__main__":
    init_database()