import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')


def count_words_in_json(json_data):
    """
    Count total words in the JSON data by iterating over all fields
    and counting words in string fields.
    """
    word_count = 0

    # Function to count words in a string
    def count_words_in_string(string):
        return len(string.split())

    # Recursively iterate through all fields in JSON
    def traverse_json(data):
        nonlocal word_count
        if isinstance(data, dict):
            for key, value in data.items():
                traverse_json(value)
        elif isinstance(data, list):
            for item in data:
                traverse_json(item)
        elif isinstance(data, str):
            word_count += count_words_in_string(data)

    traverse_json(json_data)
    return word_count

def get_Prefernce_data_and_verify_json_length():
    """
    Test case to get data from API and verify the word count is approximately 250.
    """
    print("Running test_get_Prefernce_data_and_verify_json_length")
    client = TokenClient()
    # Fetch data from the API
    get_data_url = f"{BASE_URL}/preferences"  # Modify the endpoint as necessary
    response = client.get(get_data_url)

    # Assert that the API response is OK
    assert response.status_code == 200
    
    # Get the JSON data from the response
    response_data = response.json()

    # Count the words in the returned JSON
    word_count = count_words_in_json(response_data)
    
    print(f"Total words in the returned JSON: {word_count}")

    # Check if the word count is approximately 250
    assert 260 <= word_count <= 360, f"Expected word count to be around 250, but got {word_count}."

    # Optional: Print the response for debugging
    print(f"Response: {response_data}")