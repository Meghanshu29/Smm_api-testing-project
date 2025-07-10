import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient
from pages.User_details import user_details  # Importing user_details function

BASE_URL = os.getenv('BASE_URL')

def make_profile_pic():
    """
    Test case for making a profile picture.
    This ensures that the profile picture functionality works as expected.
    """
    print("Running test_make_profile_pic")
    client = TokenClient()
    
    Data = user_details()  # Fetching user details
    Photo = Data.get('data', {}).get('photos', None)  # Adjust the key based on your actual data structure
    # Ensure the matrimonialId is available in the registered_user
    matrimonial_id = registered_user.get('matrimonialId', None)
    assert matrimonial_id is not None, "Matrimonial ID is missing in registered user."

    # Prepare the JSON data for making a profile picture
    profile_pic_data = {
        "matrimonialId": matrimonial_id,
        "profileUrl": Photo[1] if Photo else None,  # Assuming Photo contains the image data or URL
           # Replace with actual image URL or file path
    }

    # The API URL for the /make-profile-pic endpoint
    profile_pic_url = f"{BASE_URL}/profile/make-profile"

    # Send the POST request to make the profile picture
    response = client.post(profile_pic_url, json=profile_pic_data)

    # Assertions to verify the response
    assert response.status_code == 200  # Expecting a 200 OK response
    response_data = response.json()

    # Check if the response contains a success message
    assert 'success' in response_data.get('status', '').lower(), f"Profile picture update failed: {response_data.get('message')}"

    # Optional: Print the response for debugging
    print(f"Response: {response.json()}")