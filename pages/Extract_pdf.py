import os
import pytest
import requests
from conftest import registered_user
import json
from pages.Upload_bio_data import pdf_link  # Importing pdf_link from the upload_biodata_success module
from pages.Download_Biodata import download_bio_data
from client import TokenClient

BASE_URL = os.getenv('BASE_URL')
pdf_link = None

def extract_pdf():
    client = TokenClient()
    Data =download_bio_data()
    pdf_link = Data.get('pdf', None) 
    print(f"Extracted PDF Link: {pdf_link}")
    matrimonial_id = registered_user.get('matrimonialId', None)  
    assert matrimonial_id is not None, "Matrimonial ID is missing. Make sure the upload test ran first."
    assert pdf_link is not None, "PDF link is missing. Make sure the upload test ran first."
    print(f"Stored Matrimonial ID: {matrimonial_id}")
    print(f"Stored PDF Link: {pdf_link}")

    extract_pdf_url = f"{BASE_URL}/bio-data-pdf-extract"

    extract_data = {
        'matrimonialId': matrimonial_id,
        'pdfLink': pdf_link,
        'appVersion': 'TestingApp', 
    }

    response = client.post(extract_pdf_url, data=extract_data)
    assert response.status_code == 200  
    response_data = response.json()

    assert 'success' in response_data.get('status', '').lower(), f"PDF extraction failed: {response_data.get('message')}"
    print(f"Response: {response.json()}")
    
    data = response_data.get('data', None)
    assert data is not None, "'data' key is missing in the response"

    # Define the expected structure of the data
    expected_keys = [
        "name", "gender", "dateOfBirth", "placeOfBirth", "timeOfBirth", "heightCM", "weightKG", "bloodGroup",
        "complexion", "motherTongue", "maritalStatus", "subCaste", "gotra", "address", "phoneNumber", "email",
        "city", "state", "country", "zipCode", "fatherName", "motherName", "highestDegree", "institution",
        "additionalQualification", "occupation", "occupationCompany", "occupationLocation", "maxAnnualIncomeIndividual",
        "minAnnualIncomeIndividual", "hobbies", "languagesKnown", "aboutMe", "familyType", "familyBackground",
        "minAnnualIncomeFamily", "maxAnnualIncomeFamily", "nativePlace", "disability", "workingWith", "emailAddress",
        "alternateMobileNumber", "isGunnMatching", "hometown", "residentalAddress"
    ]

    # Check if all expected keys are present in the response
    for key in expected_keys:
        assert key in data, f"Missing expected key: {key} in the response data"

    # Optionally, you can verify the content of certain fields (e.g., strings, integers, arrays, etc.)
    assert isinstance(data.get('hobbies', []), list), "'hobbies' should be a list."
    assert isinstance(data.get('languagesKnown', []), list), "'languagesKnown' should be a list."

    print("Response data structure verified successfully.")

