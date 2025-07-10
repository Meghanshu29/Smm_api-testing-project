import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')


def interaction_like_dislike():
    """
     Test case for interacting with like or dislike on a matrimonial profile.
     This ensures that the like or dislike functionality works as expected.
     """
    print("Running test_interaction_like_dislike")
    client = TokenClient()
    # Ensure the matrimonialId and likedBy (userId) are available in the registered_user
    matrimonial_id = registered_user.get('matrimonialId', None)  # Fetching matrimonialId globally
    liked_by = "M381749116452"
    assert matrimonial_id is not None, "Matrimonial ID is missing in registered user."
    assert liked_by is not None, "LikedBy userId is missing in registered user."

    # Prepare the JSON data for like/dislike interaction
    interaction_data = {
        "matrimonialId": matrimonial_id,
        "status": 1,  # 1 for Like, 0 for Dislike
        "likedBy": liked_by
    }

    # The API URL for the /interaction-like-dislike endpoint
    interaction_url = f"{BASE_URL}/interaction-like-dislike"

    # Send the POST request to perform the interaction
    response = client.post(interaction_url, json=interaction_data)

    # Assertions to verify the response
    assert response.status_code == 200  # Expecting a 200 OK response
    response_data = response.json()

    # Check if the response contains a success message
    assert 'success' in response_data.get('status', '').lower(), f"Interaction failed: {response_data.get('message')}"

    # Optional: Print the response for debugging
    print(f"Response: {response.json()}")
    