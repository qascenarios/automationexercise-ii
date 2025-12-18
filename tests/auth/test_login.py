from playwright.sync_api import Page, expect
from pages.register_page import RegisterPage
from utils.config import LoginCredentials
from pages.login_page import LoginPage
from conftest import open_browser


def test_login(open_browser: Page):

    # Page Object Initialization
    register_page_reusable = RegisterPage(open_browser)
    register_page_reusable.accept_dialog()
    login_page = LoginPage(open_browser)
    # User login
    register_page_reusable.click_signup_signin_link()
    login_page.login_actions(LoginCredentials.EMAIL, LoginCredentials.PASSWORD)
    # User Login verification
    login_page.verify_successful_login()
