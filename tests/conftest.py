import pytest
from playwright.sync_api import Page

# Pytest Fixture: Browser Setup

@pytest.fixture
def open_browser(page: Page):
    """
        This fixture opens the browser and navigates to the base URL
        before each test that uses it.

        The Playwright `page` fixture is provided by pytest-playwright.
        Returning the page allows test functions to interact with the browser.
        """
    # Navigate to the application under test
    page.goto("https://automationexercise.com")

    # Return the page instance for use in tests
    return page


