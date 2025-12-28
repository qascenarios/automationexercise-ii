import pytest
from playwright.sync_api import Page, expect
from UI.pages.search_product_page import SearchProductsPage
from UI.pages.register_page import RegisterPage
from UI.utils.helpers import accept_consent_dialog
from UI.tests.conftest import open_browser


# Test Data
search_products = [
    "Fancy Green Top",
    "Cotton Mull Embroidered Dress",
    "Grunt Blue Slim Fit Jeans",
    "Winter Top"
]

# Product Search Test
@pytest.mark.parametrize("product", search_products)
def test_search_product(product, open_browser: Page):
    """
    Verify that users can search for products
    and that searched products appear in the results
    """
    # Precondition Handling
    accept_consent_dialog(open_browser)
    # Page Object Initialization
    register_page_reusable = RegisterPage(open_browser)
    search_page = SearchProductsPage(open_browser)
    # Navigate to Products Page
    search_page.click_product_element()
    # Perform Product Search
    search_page.search_for_product(product)
    search_page.click_on_search_btn()
    # Validate Search Results
    expect(search_page.get_first_searched_product()).to_contain_text(product)
    # Cleanup: Reset Search Field
    search_page.clear_search_field()
