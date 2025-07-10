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
    print("API Response received.")

    # Validate top-level keys
    assert response_data.get("status", "").lower() == "success", "API status not success"
    assert "data" in response_data, "'data' key missing in response"
    assert "preferences" in response_data["data"], "'preferences' missing under 'data'"
    assert isinstance(response_data["data"]["preferences"], list), "'preferences' is not a list"

    # Count words
    word_count = count_words_in_json(response_data)
    print(f"Total words in the returned JSON: {word_count}")

    # Range validation
    assert 260 <= word_count <= 360, f"Expected word count between 260–360, got {word_count}"

    # Optional: Print for visual inspection
    print(json.dumps(response_data, indent=2))
