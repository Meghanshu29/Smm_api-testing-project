import os
import pytest
import json
from conftest import registered_user
from client import TokenClient

BASE_URL = os.getenv('BASE_URL')


def user_details():
    """
    Verifies basic structure and keys for user profile and preferences in /user-details response.
    Focused only on simplified expected data format.
    """
    print("▶️ Running test_user_details_")

    client = TokenClient()
    user_id = registered_user.get('userId', None)
    assert user_id, "❌ User ID is missing in registered_user"

    url = f"{BASE_URL}/user-details"
    params = {
        'userId': user_id,
        'profile': True,
        'preference': True
    }

    response = client.get(url, params=params)
    assert response.status_code == 200, f"❌ Unexpected status code: {response.status_code}"

    response_data = response.json()
    assert response_data.get('status') == 'success', "❌ Status is not 'success'"
    assert response_data.get('message') == 'Details fetched successfully', "❌ Message mismatch"

    data = response_data.get('data')
    assert isinstance(data, dict), "❌ 'data' is missing or not an object"

    # ✅ Basic top-level profile fields
    expected_fields = [
        'userId', 'username','profileUrl', 'phoneNumber', 'isActive',
        'emailAddress', 'createdAt', 'preferences'
    ]

    for key in expected_fields:
        assert key in data, f"❌ Missing key in data: {key}"

    preferences = data['preferences']
    assert isinstance(preferences, dict), "❌ 'preferences' should be an object"

    # ✅ Expected preferences keys
    expected_pref_keys = [
        'maritalStatus', 'familyType', 'familyBackground', 'qualification',
        'preferredLocation', 'locationType', 'minAnnualIncome', 'maxAnnualIncome',
        'relocationWillingness', 'profession', 'hobbies', 'drinking', 'smoking',
        'dietaryHabits', 'minAge', 'maxAge', 'workingWith'
    ]

    for key in expected_pref_keys:
        assert key in preferences, f"❌ Missing key in preferences: {key}"

    print("✅ User details structure verified successfully.")
    print(json.dumps(response_data, indent=2))
    
    return response_data  # Return the response data for further use if needed
