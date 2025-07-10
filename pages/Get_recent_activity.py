import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')


def get_recent_activity():
    """
    Test case for fetching recent activity using matrimonialId.
    This ensures that the recent activities are fetched successfully for the registered user.
    """
    print("Running test_get_recent_activity")
    client = TokenClient()
    # Ensure the matrimonialId is available in the registered_user
    matrimonial_id = registered_user.get('matrimonialId', None)  # Corrected to use 'matrimonialId'
    assert matrimonial_id is not None, "User registration failed, matrimonialId is missing."

    # The API URL for getting recent activity
    get_recent_activity_url = f"{BASE_URL}/profile/recent-activity/get"

    # Prepare the query parameters to be sent in the GET request
    params = {
        'matrimonialId': matrimonial_id  # Matrimonial ID to fetch recent activity for the user
    }

    # Send the GET request to fetch recent activity
    response = client.get(get_recent_activity_url, params=params)

    # Assertions to verify the response
    assert response.status_code == 200  # Expecting a 200 OK response
    response_data = response.json()

    # Check if the response contains 'success' message
    assert 'success' in response_data.get('status', '').lower(), f"Recent activity fetch failed: {response_data.get('message')}"

    # Optional: Print the response for debugging
    print(f"Response: {response.json()}")
    
    
def load_preference_data(file_path):
    """
    Load the preference data from a JSON file.
    """
    with open(file_path, 'r') as file:
        return json.load(file)
