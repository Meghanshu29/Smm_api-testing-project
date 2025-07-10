import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Update_stage import update_stage_with_higher_value

def test_run_update_stage():
    """Test case for running update stage functionality."""
    print("Running test_run_update_stage")
    update_stage_with_higher_value()