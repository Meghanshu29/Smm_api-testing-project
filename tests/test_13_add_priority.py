import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Add_prioritydata import add_priority_weightage

def test_run_add_priority():
    """Test case for running add priority functionality."""
    print("Running test_run_add_priority")
    add_priority_weightage()