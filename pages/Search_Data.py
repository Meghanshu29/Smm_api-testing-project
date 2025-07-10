import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')

def load_search_data(filename):
    """Helper function to load search data from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)

def search():
    """
    Test case for searching using matrimonialId and preferences.
    This ensures the search functionality works as expected.
    """
    print("Running test_search")
    client = TokenClient()
    # Ensure the matrimonialId is available in the registered_user
    matrimonial_id = registered_user.get('matrimonialId', None)  # Fetching matrimonialId globally
    assert matrimonial_id is not None, "User registration failed, matrimonialId is missing."

    # Load search data from the external JSON file
    search_data = load_search_data('search_data.json')

    # Set the matrimonialId dynamically
    search_data['matrimonialId'] = matrimonial_id

    # The API URL for the /search endpoint
    search_url = f"{BASE_URL}/search"

    # Send the POST request to search
    response = client.post(search_url, json=search_data)
    print(f"Search Response: {response.json()}")  # Debugging output

    # Assertions to verify the response
    assert response.status_code == 200  # Expecting a 200 OK response
    response_data = response.json()
    
    assert 'success' in response_data.get('status', '').lower(), f"Search failed: {response_data.get('message')}"

    # Assert that 'data' is present in the response
    assert 'data' in response_data, "Expected 'data' key not found in the response."

    # Assert that 'data' is a list
    assert isinstance(response_data['data'], list), "'data' should be a list."

    # Now, let's validate the structure and content of the 'data' list.
    for user in response_data['data']:
        # Validate the user details (age, degree, employment, etc.)
        assert 'age' in user, "Age is missing in user data."
        assert 'degree' in user, "Degree is missing in user data."
        assert 'employment' in user, "Employment status is missing in user data."
        assert 'gender' in user, "Gender is missing in user data."
        assert 'height' in user, "Height is missing in user data."
        assert 'income' in user, "Income is missing in user data."
        assert 'isMatchMakingCompleted' in user, "Matchmaking status is missing in user data."
        assert 'isRequested' in user, "Request status is missing in user data."
        assert 'location' in user, "Location is missing in user data."
        assert 'matrimonialId' in user, "Matrimonial ID is missing in user data."
        assert 'maxAnnualIncome' in user, "Max annual income is missing in user data."
        assert 'minAnnualIncome' in user, "Min annual income is missing in user data."
        assert 'name' in user, "Name is missing in user data."
        
        # Validate the profileUrls (compressed and original images)
        assert 'profileUrls' in user, "Profile URLs are missing in user data."
        assert 'compressed' in user['profileUrls'], "Compressed profile image is missing."
        assert 'original' in user['profileUrls'], "Original profile image is missing."

        # Validate the userId
        assert 'userId' in user, "userId is missing in user data."

    print(f"Response: {response.json()}")  # Optional: Print the response for debugging

 