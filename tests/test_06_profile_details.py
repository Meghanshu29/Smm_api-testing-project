import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Profile_details import profile_details

def test_run_profile_details():
    """Test case for running profile details functionality."""
    print("Running test_run_profile_details")
    profile_details()