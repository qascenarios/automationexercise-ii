from playwright.sync_api import Page, expect
from pages.search_product_page import SearchProductsPage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from utils.config import LoginCredentials
from pages.cart_page import CartPage
from utils.helpers import accept_consent_dialog
from conftest import open_browser

# Test Data
products = [
    "Fancy Green Top",
    "Cotton Mull Embroidered Dress",
    "Grunt Blue Slim Fit Jeans",
    "Winter Top"
]


def test_search_product(open_browser: Page):
    """
        This test verifies that a logged-in user can:
        - Search for multiple products
        - Add them to the cart
        - Successfully see all added products in the cart
    """
    # Precondition Handling
    accept_consent_dialog(open_browser)
    # Page Object Initialization
    register_page = RegisterPage(open_browser)
    login_page = LoginPage(open_browser)
    cart_page = CartPage(open_browser)
    # User Authentication
    register_page.click_signup_signin_link()
    login_page.login_actions(
        LoginCredentials.EMAIL,
        LoginCredentials.PASSWORD
    )
    # Product Search & Cart Actions
    cart_page.open_products_page()
    cart_page.add_products_to_cart(products)
    # Verification
    cart_page.assert_products_in_cart(products)
