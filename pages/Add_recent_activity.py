import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')

def add_recent_activity():
    """
    Test case for adding a recent activity (like, view, etc.) for a user.
    This ensures that the activity is successfully added for the registered user.
    """
    print("Running add_recent_activity")
    client = TokenClient()
    # Ensure the matrimonialId is available in the registered_user
    matrimonial_id = registered_user.get('matrimonialId', None)  # Corrected to use 'matrimonialId'
    assert matrimonial_id is not None, "User registration failed, matrimonialId is missing."

    # Prepare the targetId and activityType (these should be defined as needed)
    target_id = "M331749047397"  # Example target ID (this should be another matrimonial ID or profile ID)
    activity_type = "Like"  # Example activity type (e.g., "Like", "View", etc.)

    # The API URL for the "Add Recent Activity" endpoint
    recent_activity_url = f"{BASE_URL}/profile/recent-activity/add"

    # Prepare the payload to be sent in the POST request
    activity_data = {
        "matrimonialId": matrimonial_id,  # Matrimonial ID of the registered user
        "targetId": target_id,            # Target ID for the activity (someone else's profile)
        "activityType": activity_type    # The activity (e.g., "Like", "View")
    }

    # Send the POST request to add the recent activity
    response = client.post(recent_activity_url, json=activity_data)

    # Assertions to verify the response
    assert response.status_code == 200  # Expecting a 200 OK response
    response_data = response.json()

    # Check if the response contains a success message
    assert 'success' in response_data.get('status', '').lower(), f"Activity addition failed: {response_data.get('message')}"

    # Optional: Print the response for debugging
    print(f"Response: {response.json()}")
    
    