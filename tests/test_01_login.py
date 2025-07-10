import pytest
import sys
import os

# Add the root directory of your project to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conftest import registered_matrimonial_user
from pages.Login import login_user

def test_run_login():
    """Test case for running login functionality."""
    print("Running test_run_login")
    login_user()