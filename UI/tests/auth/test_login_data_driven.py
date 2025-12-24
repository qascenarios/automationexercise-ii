from playwright.sync_api import Page
import pytest
from utils.helpers import read_json, accept_consent_dialog
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from tests.conftest import open_browser

# Test Data
login_data = read_json("utils/testdata/login_data.json")

@pytest.mark.parametrize("email, password, valid",
                         [(data["email"], data["password"], data["valid"]) for data in login_data])
def test_valid_and_invalid_login(email, password, valid, open_browser: Page):
    # Precondition Handling
    accept_consent_dialog(open_browser)
    # Page Object Initialization
    register_page_reusable = RegisterPage(open_browser)
    login_page = LoginPage(open_browser)
    # User login
    register_page_reusable.click_signup_signin_link()
    login_page.login_actions(email, password)
    # User Login verification
    if valid:
        login_page.verify_successful_login()
    else:
        login_page.verify_failed_login()
