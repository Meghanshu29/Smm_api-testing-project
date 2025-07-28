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
    assert response.status_code == 200, f"❌ Unexpected status code: {response.status_code}"
    response_data = response.json()

    # Validate top-level keys
    assert response_data.get("status", "").lower() == "success", f"❌ Status not 'success': {response_data.get('status')}"
    assert "message" in response_data, "❌ 'message' key missing"
    assert "result" in response_data, "❌ 'result' key missing"

    activities = response_data["result"]
    assert isinstance(activities, list), "❌ 'result' should be a list"
    assert len(activities) > 0, "⚠️ No recent activities found"

    for i, activity in enumerate(activities):
        assert isinstance(activity, dict), f"❌ Activity #{i+1} is not a dictionary"

        # Check required keys
        for key in ["activityId", "activityType", "activityTime", "profileDetails", "message"]:
            assert key in activity, f"❌ Missing key '{key}' in activity #{i+1}"

        # Validate activityType value
        valid_types = {"view", "like", "dislike"}
        assert activity["activityType"] in valid_types, f"❌ Invalid activityType: {activity['activityType']}"

        # Validate profileDetails
        profile = activity["profileDetails"]
        assert isinstance(profile, dict), f"❌ profileDetails in activity #{i+1} is not a dict"
        for pkey in ["id", "firstName", "profileUrl"]:
            assert pkey in profile, f"❌ Missing '{pkey}' in profileDetails of activity #{i+1}"

    print("✅ All recent activity records validated successfully.")
    print("🔍 Sample response preview:")
    print(json.dumps(response_data, indent=2))
