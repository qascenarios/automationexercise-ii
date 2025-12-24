import random
import string
import json
from playwright.sync_api import Page

def generate_random_email():
    """
        Generates a random email address for test execution.

        This is useful for scenarios like user registration,
        where a unique email address is required for every test run.
    """
    return f"tester_{random.randint(10,999)}@mail.com"

def read_json(file_path):
    """
        Reads and returns data from a JSON file.

        Args:
            file_path (str): Path to the JSON file.

        Returns:
            dict or list: Parsed JSON data from the file.
    """
    file = open(file_path, 'r')
    return json.load(file)

def accept_consent_dialog(page: Page):
    """
    Accepts the consent/cookie dialog if it is visible.

    Args:
        page (Page): Playwright page object
    """
    dialog = page.get_by_role("button", name="Consent")

    # Check visibility before clicking to avoid test failure
    if dialog.is_visible():
        dialog.click()


