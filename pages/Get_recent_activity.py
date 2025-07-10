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
    assert 'success' in response_data.get('status', '').lower(), f"Fetch failed: {response_data.get('message')}"
    assert 'result' in response_data, "No result field in response"
    assert isinstance(response_data['result'], list), "Result is not a list"

    activities = response_data['result']
    assert len(activities) > 0, "No recent activity found"

    # Sample verification: checking one or more expected fields
    for activity in activities:
        assert 'activityId' in activity, "Missing activityId"
        assert 'activityType' in activity, "Missing activityType"
        assert activity['activityType'] in ['view', 'like', 'dislike'], f"Unexpected activityType: {activity['activityType']}"
        assert 'message' in activity, "Missing message"
        assert 'profileDetails' in activity, "Missing profileDetails"
        assert 'id' in activity['profileDetails'], "Missing profile id in profileDetails"
    

    print("✅ All recent activity records are valid.")
    print(f"Response: {json.dumps(response_data, indent=2)}")
    
def load_preference_data(file_path):
    """
    Load the preference data from a JSON file.
    """
    with open(file_path, 'r') as file:
        return json.load(file)
