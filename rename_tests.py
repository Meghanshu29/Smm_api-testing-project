import os
import glob

# Define the systematic naming for test cases
test_mappings = [
    ("test_case_01_login.py", "test_01_login.py"),
    ("test_TestCase-02-Upload_biodata.py", "test_02_upload_biodata.py"),
    ("test_TestCase-03-Download_biodata.py", "test_03_download_biodata.py"),
    ("test_TestCase-04-Extract_pdf.py", "test_04_extract_pdf.py"),
    ("test_TestCase-05-Upload_photo.py", "test_05_upload_photo.py"),
    ("test_TestCase-06profile_details.py", "test_06_profile_details.py"),
    ("test_TestCase-07-Set_Profile_pic.py", "test_07_set_profile_pic.py"),
    ("test_TestCase-08-User_details.py", "test_08_user_details.py"),
    ("test_TestCase-09-Search.py", "test_09_search.py"),
    ("test_TestCase-10-Get_General_data.py", "test_10_general_data.py"),
    ("test_TestCase-11-categories.py", "test_11_categories.py"),
    ("test_TestCase-12-add_activity.py", "test_12_add_activity.py"),
    ("test_TestCase-13-Add_priority.py", "test_13_add_priority.py"),
    ("test_TestCase-14-get_activity.py", "test_14_get_activity.py"),
    ("test_TestCase-15-version.py", "test_15_version.py"),
    ("test_TestCase-16-Update_stage.py", "test_16_update_stage.py"),
    ("test_TestCase-17-Get_Preference_data.py", "test_17_get_preference_data.py"),
    ("test_TestCase-18-Update_preference.py", "test_18_update_preference.py"),
    ("test_TestCase-19-Matchmaking_request.py", "test_19_matchmaking_request.py"),
    ("test_TestCase-20_publish_match.py", "test_20_publish_match.py"),
    ("test_TestCase-21_matchmaking_results.py", "test_21_matchmaking_results.py"),
    ("test_TestCase-22-Interactions.py", "test_22_interactions.py"),
    ("test_TestCase-23-Get_stage.py", "test_23_get_stage.py"),
    ("test_TestCase-24-Delete_profile_photo.py", "test_24_delete_profile.py"),
    ("test_clear_cache_25.py", "test_25_clear_cache.py"),
    ("test_case_About_me_26.py", "test_26_about_me.py"),
    ("test_categories.py", "test_27_categories.py"),
    ("test_Company_info.py", "test_28_company_info.py"),
    ("test_subscribe.py", "test_29_subscribe.py"),
    ("test_platform.py", "test_30_platform.py")
]

# Change to tests directory
os.chdir("tests")

# Rename files
for old_name, new_name in test_mappings:
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"Renamed: {old_name} -> {new_name}")
    else:
        print(f"File not found: {old_name}")

print("Finished renaming all test files!")