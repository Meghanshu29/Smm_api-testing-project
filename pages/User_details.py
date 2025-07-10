import os
import pytest
import requests
from conftest import registered_user  # Assuming you have 'registered_user' with valid data
import json
from client import TokenClient

BASE_URL = os.getenv('BASE_URL')

def user_details():
    """
    Test case for getting user details including profile and preferences.
    """
    print("Running test_get_user_details")
    client = TokenClient()
    # Fetching the userId globally, or you can hardcode it if needed
    user_id = registered_user.get('userId', None)
    assert user_id is not None, "User ID is missing."

    # API URL for getting user details
    user_details_url = f"{BASE_URL}/user-details"

    # Prepare parameters for the GET request
    params = {
        'userId': user_id,
        'profile': True,  # Fetch profile details
        'preference': True  # Fetch preference details
    }

    # Send GET request
    response = client.get(user_details_url, params=params)

    # Verify the response status code
    assert response.status_code == 200, f"Failed to get user details, status code: {response.status_code}"
    
    # Get the JSON response data
    response_data = response.json()

    # Assert the presence of the required fields in the response
    assert response_data.get('status') == 'success', "Status is not success."
    assert response_data.get('message') == 'Details fetched successfully', "Message mismatch."
    
    # Assert that data is present in the response
    data = response_data.get('data', {})
    assert data, "Data is missing in the response."

    # Check if profile and preferences are returned in the response
    profile = data.get('profile', {})
    preferences = data.get('preferences', {})
    
    assert profile, "Profile details are missing in the response."
    assert preferences, "Preferences details are missing in the response."

    # Optionally, you can assert individual fields in profile and preferences
    assert 'userId' in profile, "userId is missing in profile details."
    
    # Validate that the userId in the profile matches the registered userId
    assert profile.get('userId') == user_id, f"User ID mismatch in profile. Expected {user_id}, got {profile.get('userId')}."
    
    # Validate the structure of the profile JSON
    expected_profile_keys = [
        'matrimonialId', 'firstName', 'gender', 'dateOfBirth', 'birthPlace', 
        'heightCm', 'weightKg', 'email', 'bloodGroup', 'complexion', 
        'maritalStatus', 'fatherName', 'motherName', 'nativePlace', 
        'siblingCount', 'familyIncomeInr', 'familyType', 'familyBackground', 
        'qualification', 'additionalQualification', 'occupation', 'occupationCompany', 
        'occupationLocation', 'workingWith', 'annualIncomeInr', 'subCaste', 'gotra', 
        'hobbies', 'manglik', 'isManglik', 'dietary', 'drinking', 'smoking', 'userId', 
        'subscribeToken', 'aboutMe', 'birthTime', 'disability', 'languagesKnown', 
        'address', 'alternatePhone', 'isGunnMatchingImportant', 'phone', 'country', 
        'city', 'state', 'minAnnualIncome', 'maxAnnualIncome', 'isQuestionnaireComplete', 
        'income', 'location', 'age'
    ]
    
    for key in expected_profile_keys:
        assert key in profile, f"Missing expected key: {key} in profile details"

    # Validate the structure of the preferences JSON
    expected_preferences_keys = [
        'userId', 'maritalStatus', 'familyType', 'familyBackground', 'qualification', 
        'preferredLocation', 'locationType', 'minAnnualIncome', 'maxAnnualIncome', 
        'relocationWillingness', 'profession', 'hobbies', 'drinking', 'smoking', 
        'dietaryHabits', 'minAge', 'maxAge', 'workingWith', 'nonNegotiables'
    ]
    
    for key in expected_preferences_keys:
        assert key in preferences, f"Missing expected key: {key} in preferences details"

    # If no exceptions were raised, print the JSON response
    print(f"Response Data: {json.dumps(response_data, indent=2)}")

    return response_data
