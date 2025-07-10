import sys
import os
import pytest
from conftest import registered_user
import json
from client import TokenClient

BASE_URL = os.getenv('BASE_URL')

def disable_user():
    
    user_id = registered_user.get('userId', None)  # Get userId from registered_user
    assert user_id is not None, "User registration failed, userId is missing."
    client = TokenClient()
    response = client.delete(f"{BASE_URL}/disable-user", params={"userId": user_id})
    assert response.status_code == 200, f"Failed to disable user with status code: {response.status_code}"
    response_data = response.json()
    assert response_data.get('status') == 'success', f"Expected status 'success', but got {response_data.get('status')}"
    assert response_data.get('message') == 'User deleted successfully', f"Expected message 'User deleted successfully', but got {response_data.get('message')}"
    return response_data
