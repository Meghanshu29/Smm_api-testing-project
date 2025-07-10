import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Matchmaking_result import matchmaking_results

def test_run_matchmaking_results():
    """Test case for running matchmaking results functionality."""
    print("Running test_run_matchmaking_results")
    matchmaking_results()