import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')

def load_priority_data(file_path):
    """
    Helper function to load priority weightage JSON data from an external file.
    """
    with open(file_path, 'r') as f:
        return json.load(f)

def add_priority_weightage():
    """
    Test case to add priority weightage for the registered matrimonial ID.
    It verifies that the priorities are successfully updated.
    """
    print("Running add_priority_weightage")
    client = TokenClient()
    # Ensure the matrimonialId is available from the registered_user
    matrimonial_id = registered_user.get('matrimonialId', None)  # Fetching matrimonialId
    assert matrimonial_id is not None, "User registration failed, matrimonialId is missing."

    # Load the priority weightage data from an external JSON file
    priority_data = load_priority_data('priority_data.json')  # Load from an external file
    
    # Update the priority data with the matrimonialId
    priority_data["matrimonialId"] = matrimonial_id

    # The API URL for adding priority weightage
    add_priority_weightage_url = f"{BASE_URL}/add/priority-weightage"

    # Send the POST request to add priority weightage
    response = client.post(add_priority_weightage_url, json=priority_data)

    # Assertions to verify the response
    assert response.status_code == 200  # Expecting a 200 OK response
    response_data = response.json()

    # Check if the response contains 'success' message
    assert 'success' in response_data.get('status', '').lower(), f"Priority weightage update failed: {response_data.get('message')}"

    # Optional: Print the response for debugging
    print(f"Response: {response.json()}")
    
