import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Update_preference import update_preference

def test_run_update_preference():
    """Test case for running update preference functionality."""
    print("Running test_run_update_preference")
    update_preference()