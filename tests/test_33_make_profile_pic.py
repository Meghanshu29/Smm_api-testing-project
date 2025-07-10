import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Make_Profile_pic import make_profile_pic


def test_make_profile_pic():
    make_profile_pic()