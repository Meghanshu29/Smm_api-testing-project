import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.Subscribe import subscribe_email_success

def test_subscribe_user():
    """Test case for subscribing a user."""
    print("Running test_subscribe_user")
    subscribe_email_success()