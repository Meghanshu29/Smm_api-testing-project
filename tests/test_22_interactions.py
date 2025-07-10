import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Interactions import interaction_like_dislike

def test_run_interactions():
    """Test case for running interactions functionality."""
    print("Running test_run_interactions")
    interaction_like_dislike()