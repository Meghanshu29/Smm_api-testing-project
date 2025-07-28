import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Matchmaking_request import matchmaking_request
@pytest.mark.skip(reason="Skipping test for now")
def test_run_matchmaking():
    """Test case for running matchmaking functionality."""
    print("Running test_run_matchmaking")
    matchmaking_request()