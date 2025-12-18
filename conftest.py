
import pytest
from playwright.sync_api import Page


@pytest.fixture
def open_browser(page: Page):
    page.goto("https://automationexercise.com/login")
    return page


