import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Get_recent_activity import get_recent_activity

def test_run_get_activity():
    """Test case for running get activity functionality."""
    print("Running test_run_get_activity")
    get_recent_activity()