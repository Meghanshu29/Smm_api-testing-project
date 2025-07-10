import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Set_Profile import set_profile_picture

def test_run_set_profile_pic():
    """Test case for running set profile picture functionality."""
    print("Running test_run_set_profile_pic")
    set_profile_picture()