import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Delete_profile import delete_profile_Photo

def test_run_delete_profile():
    """Test case for running delete profile functionality."""
    print("Running test_run_delete_profile")
    delete_profile_Photo()