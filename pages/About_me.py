import pytest
import sys
import os
import requests
from conftest import registered_user
import json
from pages.User_details import user_details
import json
from client import TokenClient

BASE_URL = os.getenv('BASE_URL')

import os
import requests
from conftest import registered_user
import json

BASE_URL = os.getenv('BASE_URL')

def about_me():
    """
    Test case for verifying the 'About Me' information response from the /get-about-me endpoint.
    This ensures that the status, message, and 'About Me' information data are correctly returned.
    """
    print("Running test_about_me")
    client = TokenClient()
    # Assuming user_details() is fetching necessary data like profile information
    User = user_details()
    print(f"Data: {User}")

    # Get profile data from the previously fetched data
    Data = User.get('data', None)  # Adjust the key based on your actual data structure
    Profile = Data.get('profile', None) if Data else None  # Adjust the key based on your actual data structure
    # Ensure profile data is not empty
    assert Profile is not None, "Profile data is empty or not found."

    # The API URL for fetching 'about me' information
    about_me_url = f"{BASE_URL}/get-about-me-samples"  # Replace with your actual endpoint

    # Send the POST request to fetch 'About Me' information (If it is meant to be POST, we will use POST)
    response = client.post(about_me_url, json={"userProfileDetails": Profile})

    # Debug: Print the response for inspection
    print(f"Response: {response.json()}")

    # Assertions to verify the response
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"  # Expecting a 200 OK response
    
    # Parse the response
    response_data = response.json()

    # Check if the response contains 'status' and it equals 'success'
    assert response_data.get('status') == 'success', f"Expected status 'success', but got {response_data.get('status')}"

    

