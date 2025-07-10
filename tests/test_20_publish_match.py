import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Publish_match import publish_match

def test_run_publish_match():
    """Test case for running publish match functionality."""
    print("Running test_run_publish_match")
    publish_match()