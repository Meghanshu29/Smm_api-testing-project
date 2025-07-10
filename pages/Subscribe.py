import os
import pytest
import requests
import json
import os
import requests
from conftest import registered_user

BASE_URL = os.getenv('BASE_URL')

from pages.Profile_details import profile_details  # Import the already defined function
from pages.User_details import user_details  # Import the user details function
from client import TokenClient

 # Use your API's base URL

def subscribe_email_success():
    """
    Test case for successfully subscribing a user with email, phone, and name.
    """
    client = TokenClient()

    # Prepare the payload for the POST request
    data = {
        "email": "testuser@example.com",
        "phone": "1234567890",
        "name": "Test User",
        "msg": "Looking forward to subscribing!"
    }

    # Make the POST request to the /subscribeForSite endpoint
    response = client.post(f"{BASE_URL}/subscribeForSite", json=data)

    # Print the response for debugging
    print(f"Response: {response.json()}")

    # Verify that the status code is 200 (OK)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    # Parse the response data
    response_data = response.json()

    # Check if the response contains success status
    assert response_data.get('status') == 'success', f"Expected 'success', but got {response_data.get('status')}"

    