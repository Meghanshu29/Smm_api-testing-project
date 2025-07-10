import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Add_recent_activity import add_recent_activity

def test_run_add_activity():
    """Test case for running add activity functionality."""
    print("Running test_run_add_activity")
    add_recent_activity()