import os
import requests
from conftest import registered_user

BASE_URL = os.getenv('BASE_URL')

# Assuming you already have this function defined elsewhere in your code
# This function should fetch user data including 'photos'
from pages.Profile_details import profile_details  # Import the already defined function
from pages.User_details import user_details  # Import the user details function
from client import TokenClient

def set_profile_picture():
    """
    Test case for setting the profile picture using the fetched profile URL.
    This will ensure that the correct profile picture is set for the user.
    """
    print("Running test_set_profile_picture")
    client = TokenClient()
    # Call the existing get_user_details function to fetch user data
    # It should return the photos list
    user_data = user_details()  # Assuming this function is already defined to fetch the user data

    # Ensure the photos are available in the response
    Data = user_data.get('data', None)
    photos = Data.get('photos', None) if Data else None
    assert photos is not None and len(photos) > 0, "Photos are not found or empty. Ensure the Get User API is working."

    print(f"Photos fetched: {photos}")
    
    # Pick the first photo from the list (you can change the logic to pick any other photo)
    profile_url = photos[0]  # Assuming the first photo should be used as the profile picture
    
    # Ensure the URL is valid
    assert profile_url.startswith("https://"), "Invalid profile photo URL."

    print(f"Profile URL to be set: {profile_url}")
    
    # Prepare the API URL for setting the profile picture
    set_profile_url = f"{BASE_URL}/profile/make-profile"
    
    # Prepare the request data to set the profile picture
    data = {
        'matrimonialId': registered_user.get('matrimonialId', None),  # Use matrimonialId as profileId
        'profileUrl': profile_url  # The profile URL fetched from the user details API
    }
    
    # Send the POST request to set the profile picture
    response = client.post(set_profile_url, json=data)
    
    # Assertions to verify the response
    assert response.status_code == 200, f"Failed to set profile picture, status code: {response.status_code}"
    
    response_data = response.json()
    
    # Check if the response contains 'success' message
    assert 'success' in response_data.get('status', '').lower(), f"Profile picture update failed: {response_data.get('message')}"
    
    print(f"Response: {response.json()}")

