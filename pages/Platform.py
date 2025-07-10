import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')
pdf_link = None

def platform_get():
    """
    Test case for the GET method of the /platform endpoint with a valid userId.
    This should return the platform associated with the user.
    """
    user_id = registered_user.get('userId', None)
    assert user_id is not None, "User registration failed, userId is missing."
    client = TokenClient()
    response = client.get(f"{BASE_URL}/platform", params={"userId": user_id})

    # Print response for debugging
    print(f"GET Response: {response.json()}")
    

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response contains status 'success'
    response_data = response.json()
    assert response_data['status'] == 'success', f"Expected status 'success', got {response_data['status']}"

    # Check if the platform information is returned
    assert 'platform' in response_data, "Platform information is missing in the response."

def platform_post():
    """
    Test case for the POST method of the /platform endpoint with a valid userId.
    This should update the platform associated with the user.
    """
    # Ensure userId is available in registered_user
    user_id = registered_user.get('userId', None)
    assert user_id is not None, "User registration failed, userId is missing."
    
    # Create a TokenClient instance for authenticated requests
    client = TokenClient()
    # Example platform data to update
    platform_data = {
        "platform": "Testing Platform",  # Your platform value
        "userId": user_id  # User ID from registered_user
    }

    # Make the POST request to update the platform
    response = client.post(f"{BASE_URL}/platform", json=platform_data)
    # Ensure the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Ensure the response contains status 'success'
    response_data = response.json()
    assert response_data.get('status') == 'success', f"Expected status 'success', got {response_data.get('status')}"

    # Optionally, verify the platform has been updated (you can check the response or verify via GET request)
    assert 'platform' in response_data, "Platform information is missing in the response."
    print(f"POST Response: {response.json()}")