import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Get_Stage import get_stage

def test_run_get_stage():
    """Test case for running get stage functionality."""
    print("Running get_stage")
    get_stage()