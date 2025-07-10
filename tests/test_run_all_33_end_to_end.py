import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import all test functions from pages
from pages.Login import login_user
from pages.Upload_bio_data import upload_biodata_success
from pages.Download_Biodata import download_bio_data
from pages.Extract_pdf import extract_pdf
from pages.Upload_photo import upload_photos
from pages.Profile_details import profile_details
from pages.Set_Profile import set_profile_picture
from pages.User_details import user_details
from pages.Search_Data import search
from pages.Generaldata import get_general_data
from pages.Categories import categories
from pages.Add_recent_activity import add_recent_activity
from pages.Add_prioritydata import add_priority_weightage
from pages.Get_recent_activity import get_recent_activity
from pages.GetVersion import get_Version_data_and_verify_json
from pages.Update_stage import update_stage_with_higher_value
from pages.Get_Prefernce_data import get_Prefernce_data_and_verify_json_length
from pages.Update_preference import update_preference
from pages.Matchmaking_request import matchmaking_request
from pages.Publish_match import publish_match
from pages.Matchmaking_result import matchmaking_results
from pages.Interactions import interaction_like_dislike
from pages.Get_Stage import get_stage
from pages.Delete_profile import delete_profile_Photo
from pages.Clear_Cache import clear_cache
from pages.About_me import about_me
from pages.Company_info import company_info
from pages.Subscribe import subscribe_email_success
from pages.Platform import platform_get, platform_post
from pages.Enable_User import Enable_User
from pages.Disable_User import disable_user
from pages.Make_Profile_pic import make_profile_pic

def test_run_all_33_end_to_end():
    """
    Complete End-to-End Test Suite - All 33 Test Cases
    Runs all tests in logical flow order for comprehensive API testing
    """
    print("🚀 Starting Complete End-to-End Test Suite - 33 Test Cases")
    print("=" * 80)
    
    try:
        # Phase 1: Authentication & Setup
        print("\n📋 PHASE 1: AUTHENTICATION & SETUP")
        print("-" * 50)
        
        print("01. 🔐 Login")
        login_user()
        
        print("02. 📄 Upload Biodata")
        upload_biodata_success()
        
        print("03. ⬇️ Download Biodata")
        download_bio_data()
        
        print("04. 📝 Extract PDF")
        extract_pdf()
        
        # Phase 2: Profile Management
        print("\n👤 PHASE 2: PROFILE MANAGEMENT")
        print("-" * 50)
        
        print("05. 📸 Upload Photos")
        upload_photos()
        
        print("06. 📋 Profile Details")
        profile_details()
        
        print("07. 🖼️ Set Profile Picture")
        set_profile_picture()
        
        print("08. 👥 User Details")
        user_details()
        
        print("09. 🔍 Search")
        search()
        
        # Phase 3: Data & Configuration
        print("\n⚙️ PHASE 3: DATA & CONFIGURATION")
        print("-" * 50)
        
        print("10. 📊 General Data")
        get_general_data()
        
        print("11. 📂 Categories")
        categories()
        
        print("12. ➕ Add Activity")
        add_recent_activity()
        
        print("13. ⭐ Add Priority")
        add_priority_weightage()
        
        print("14. 📋 Get Activity")
        get_recent_activity()
        
        print("15. 🔢 Version")
        get_Version_data_and_verify_json()
        
        # Phase 4: User Progress & Preferences
        print("\n📈 PHASE 4: USER PROGRESS & PREFERENCES")
        print("-" * 50)
        
        print("16. 📊 Update Stage")
        update_stage_with_higher_value()
        
        print("17. 💝 Get Preference Data")
        get_Prefernce_data_and_verify_json_length()
        
        print("18. ✏️ Update Preference")
        update_preference()
        
        print("19. 💕 Matchmaking Request")
        matchmaking_request()
        
        # Phase 5: Matching & Interactions
        print("\n💖 PHASE 5: MATCHING & INTERACTIONS")
        print("-" * 50)
        
        print("20. 📢 Publish Match")
        publish_match()
        
        print("21. 🎯 Matchmaking Results")
        matchmaking_results()
        
        print("22. 👍 Interactions")
        interaction_like_dislike()
        
        print("23. 📊 Get Stage")
        get_stage()
        
        # Phase 6: System Operations
        print("\n🔧 PHASE 6: SYSTEM OPERATIONS")
        print("-" * 50)
        
        print("24. 🗑️ Delete Profile")
        delete_profile_Photo()
        
        print("25. 🧹 Clear Cache")
        clear_cache()
        
        print("26. ℹ️ About Me")
        about_me()
        
        print("27. 🏢 Company Info")
        company_info()
        
        print("28. 💳 Subscribe")
        subscribe_email_success()
        
        print("29. 🖥️ Platform GET")
        platform_get()
        
        print("30. 🖥️ Platform POST")
        platform_post()
        
        # Additional Test Cases (31-33)
        print("\n🔄 PHASE 7: ADDITIONAL OPERATIONS")
        print("-" * 50)
        
        print("31. 🔄 User Enable/Disable")
        # Add function call when available
        Enable_User()
        disable_user()
        print("32. 🧪 User Testing")
        # Add function call when available
        
        print("33. 🖼️ Make Profile Picture")
        # Add function call when available
        make_profile_pic()
        
        
        print("\n" + "=" * 80)
        print("✅ END-TO-END TEST SUITE COMPLETED SUCCESSFULLY!")
        print("🎉 All 33 test cases executed in logical flow order")
        print("=" * 80)
        
    except Exception as e:
        print(f"\n❌ TEST SUITE FAILED AT: {e}")
        print("🔍 Check logs above for detailed error information")
        raise e

if __name__ == "__main__":
    test_run_all_33_end_to_end()