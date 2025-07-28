import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient

BASE_URL = os.getenv('BASE_URL')

def count_words_in_json(json_data):
    """
    Count total words in the JSON data by iterating over all string fields.
    """
    word_count = 0

    def count_words_in_string(string):
        return len(string.split())

    def traverse_json(data):
        nonlocal word_count
        if isinstance(data, dict):
            for value in data.values():
                traverse_json(value)
        elif isinstance(data, list):
            for item in data:
                traverse_json(item)
        elif isinstance(data, str):
            word_count += count_words_in_string(data)

    traverse_json(json_data)
    return word_count


def get_preference_data_and_verify_json_length():
    """
    Test case to verify preference data is returned successfully
    and contains a reasonable word count.
    """
    print("Running test_get_preference_data_and_verify_json_length")
    client = TokenClient()

    # API call
    get_data_url = f"{BASE_URL}/preferences"
    response = client.get(get_data_url)

    # Status code check
    assert response.status_code == 200

    # Parse response JSON
    response_data = response.json()
    print("✅ API response received.")

    # Validate top-level structure
    assert response_data.get("status") == "success", "Missing or invalid 'status'"
    assert response_data.get("message"), "Missing or empty 'message'"
    assert "data" in response_data and isinstance(response_data["data"], dict), "'data' key missing or invalid"
    
    data = response_data["data"]

    # Validate user profile presence
    assert "profile" in data, "Missing 'profile' key"
    assert "preferences" in data, "Missing 'preferences' key"

    # Validate preference type
    assert isinstance(data["preferences"], dict), "'preferences' should be an object"

    # Optional: Validate photos and other expected fields exist
    assert isinstance(data.get("photos", []), list), "'photos' must be a list"

    # Count total words in JSON response
    word_count = count_words_in_json(response_data)
    print(f"📝 Word count in response JSON: {word_count}")
    assert 260 <= word_count <= 360, f"Expected word count between 260–360, got {word_count}"

    # Optional: print formatted output for inspection
    print("🔍 JSON Preview:")
    print(json.dumps(response_data, indent=2))

    print("🎉 Test passed: Preference data is valid and well-structured.")