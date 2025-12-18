import json

import pytest
from playwright.sync_api import Page, expect
from conftest import open_browser
from pages.account_info_page import AccountInformationPage
from pages.register_page import RegisterPage
from utils.helpers import generate_random_email


def read_json(file_path):
    file = open(file_path, 'r')
    return json.load(file)


#@pytest.mark.parametrize("")
def test_register_new_user(open_browser: Page):

    # Test Data Setup
    random_email = generate_random_email()
    acct_info = read_json("testdata/register.json")
    # Page Object Initialization
    register = RegisterPage(open_browser)
    account_info_page = AccountInformationPage(open_browser)
    # Precondition Handling
    register.accept_dialog()
    # User Registration
    register.register_actions("tester", random_email)
    # Account Information Submission
    account_info_page.account_info_actions(
        acct_info["password"],
        acct_info["firstname"],
        acct_info["lastname"],
        acct_info["address1"],
        acct_info["country"],
        acct_info["state"],
        acct_info["city"],
        acct_info["zipcode"],
        acct_info["phone"]
    )

    # Verification
    register.verify_successful_registration("Account Created!")



