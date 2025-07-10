import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')
pdf_link = None

def load_preference_data(file_path):
    """
    Load the preference data from a JSON file.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

def update_preference():
    """
    Test case for updating the user preferences using PATCH request.
    This ensures that the preferences are updated successfully.
    """
    print("Running test_update_preference")
    client = TokenClient()
    # Ensure the userId is available in the registered_user
    user_id = registered_user.get('userId', None)  # Corrected to use 'userId'
    assert user_id is not None, "User registration failed, userId is missing."

    # Load the preference data from the JSON file
    preference_data = load_preference_data("preferences_data.json")
    
    # Update the userId and matrimonialId in the preference data to match the registered user
    preference_data["preference"]["userId"] = user_id
    preference_data["matrimonial"]["matrimonialId"] = registered_user.get("matrimonialId")
    
    Data=preference_data.get("preference", {})
    # The API URL for the "Update Preference" endpoint
    update_preference_url = f"{BASE_URL}/patch/preference"

    # Send the PATCH request to update preferences
    response = client.patch(update_preference_url, json=Data)

    # Assertions to verify the response
    assert response.status_code == 200  # Expecting a 200 OK response
    response_data = response.json()

    # Check if the response contains a success message
    assert 'success' in response_data.get('status', '').lower(), f"Preference update failed: {response_data.get('message')}"

    # Optional: Print the response for debugging
    print(f"Response: {response.json()}")
