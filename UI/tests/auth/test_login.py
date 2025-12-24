from playwright.sync_api import Page
from UI.pages.register_page import RegisterPage
from UI.utils.config import LoginCredentials
from UI.pages.login_page import LoginPage
from UI.tests.conftest import open_browser
from UI.utils.helpers import accept_consent_dialog

def test_login(open_browser: Page):
    # Precondition Handling
    accept_consent_dialog(open_browser)
    # Page Object Initialization
    register_page_reusable = RegisterPage(open_browser)
    login_page = LoginPage(open_browser)
    # User login
    register_page_reusable.click_signup_signin_link()
    login_page.login_actions(LoginCredentials.EMAIL, LoginCredentials.PASSWORD)
    # User Login verification
    login_page.verify_successful_login()
