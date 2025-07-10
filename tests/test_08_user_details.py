import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.User_details import user_details

def test_run_user_details():
    """Test case for running user details functionality."""
    print("Running test_run_user_details")
    user_details()