import os
import requests
from conftest import registered_user  # Assuming you have registered_user with valid data
from pages.User_details import user_details  # Assuming this function fetches user details
from client import TokenClient

BASE_URL = os.getenv('BASE_URL')

def delete_profile_Photo():
    """
    Test case for deleting the user's profile.
    This will send a request to delete the profile using the fetched matrimonialId and profileUrl.
    """
    print("Running delete_profile")
    client = TokenClient()

    # Fetching the user ID and matrimonialId globally
    matrimonial_id = registered_user.get('matrimonialId', None)
    assert matrimonial_id is not None, "Matrimonial ID is missing."

    # Fetch the user details, including the profileUrl (this should return data including 'profileUrl')
    user_data = user_details()  # Assuming this function fetches the user data
    profile_url = user_data.get('data', {}).get('profileUrl', None)

    assert profile_url is not None, "Profile URL is missing."

    # Prepare the API URL for deleting the profile
    delete_profile_url = f"{BASE_URL}/profile/delete-profile"

    # Prepare the data to send in the POST request
    data = {
        'matrimonialId': matrimonial_id,  # Matrimonial ID from the registered user
        'profileUrl': profile_url         # The profile URL fetched from the user details
    }

    # Send the POST request to delete the profile
    response = client.post(delete_profile_url, json=data)

    # Verify the response status code
    assert response.status_code == 200, f"Failed to delete profile, status code: {response.status_code}"

    # Get the JSON response data
    response_data = response.json()

    # Assert the presence of a success message in the response
    assert 'success' in response_data.get('status', '').lower(), f"Profile deletion failed: {response_data.get('message')}"

    print(f"Response Data: {response_data}")

    # Optionally, verify if the profile has been deleted successfully by checking the response message
   
