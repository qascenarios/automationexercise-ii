from playwright.sync_api import Page, expect
import pytest, json
from pages.register_page import RegisterPage
from utils.config import LoginCredentials
from pages.login_page import LoginPage
from conftest import open_browser

with open("testdata/login_data.json") as f:
    login_data = json.load(f)


@pytest.mark.parametrize("email, password, valid",
                         [(data["email"], data["password"], data["valid"]) for data in login_data])
def test_valid_and_invalid_login(email, password, valid, open_browser: Page):
    # Page Object Initialization
    register_page_reusable = RegisterPage(open_browser)
    register_page_reusable.accept_dialog()
    login_page = LoginPage(open_browser)
    # User login
    register_page_reusable.click_signup_signin_link()
    login_page.login_actions(email, password)
    # User Login verification
    if valid:
        login_page.verify_successful_login()
    else:
        login_page.verify_failed_login()
