from playwright.sync_api import Page
from tests.conftest import open_browser
from pages.account_info_page import AccountInformationPage
from pages.register_page import RegisterPage
from utils.helpers import generate_random_email, accept_consent_dialog


def test_register_new_user(open_browser: Page):
    # Precondition Handling
    accept_consent_dialog(open_browser)
    # Test Data Setup
    random_email = generate_random_email()
    # Page Object Initialization
    register = RegisterPage(open_browser)
    account_info_page = AccountInformationPage(open_browser)
    # User Registration
    register.register_actions("tester", random_email)
    # Account Information Submission
    account_info_page.account_info_actions(
        "tester2025#",
        "Sulaimon",
        "Ekundayo",
        "22, Chedlin Avenue",
        "Canada",
        "Toronto",
        "Toronto Boulevard",
        "202025",
        "+154654422",
    )

    # Verification
    register.verify_successful_registration("Account Created!")



