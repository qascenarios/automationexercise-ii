from playwright.sync_api import Page, expect
from UI.pages.register_page import RegisterPage
from UI.pages.login_page import LoginPage
from UI.utils.config import LoginCredentials
from UI.pages.cart_page import CartPage
from UI.pages.delete_page import DeletePage
from UI.utils.helpers import accept_consent_dialog

def test_delete_products_from_cart(open_browser: Page):
    # Precondition Handling
    accept_consent_dialog(open_browser)
    # Page Object Initialization
    register_page = RegisterPage(open_browser)
    login_page = LoginPage(open_browser)
    cart_page = CartPage(open_browser)
    delete_page = DeletePage(open_browser)
    # User Authentication
    register_page.click_signup_signin_link()
    login_page.login_actions(LoginCredentials.EMAIL, LoginCredentials.PASSWORD)
    cart_page.click_cart_element()
    # Delete products in cart
    delete_page.delete_product_from_cart(["Blue Top", "Fancy Green Top"])
