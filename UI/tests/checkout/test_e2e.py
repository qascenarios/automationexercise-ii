from playwright.sync_api import Page
from UI.pages.cart_page import CartPage
from UI.pages.checkout_page import CheckoutPage
from UI.pages.login_page import LoginPage
from UI.pages.register_page import RegisterPage
from UI.utils.helpers import read_json
from UI.utils.helpers import accept_consent_dialog
from UI.utils.config import LoginCredentials

# Test Data
card = read_json("UI/utils/testdata/card_info.json")
products = read_json("UI/utils/testdata/products.json")["products"]

def test_end_to_end_test_for_customer_lifecycle(open_browser: Page):
    """
        End-to-End Test: Customer Lifecycle

        This test covers a complete customer journey on the application:
        - Accept cookie/consent dialog
        - Login with existing credentials
        - Search and add multiple products to the cart
        - Proceed to checkout
        - Enter card details and place an order
        - Verify successful order placement
        - Logout from the application
    """
    # Precondition Handling
    accept_consent_dialog(open_browser)
    # Page Object Initialization
    register_page_reusable = RegisterPage(open_browser)
    login_page_reusable = LoginPage(open_browser)
    cart_page_reusable = CartPage(open_browser)
    checkout_page = CheckoutPage(open_browser)
    # User Authentication
    register_page_reusable.click_signup_signin_link()
    login_page_reusable.login_actions(LoginCredentials.EMAIL, LoginCredentials.PASSWORD)
    # Product Search & Cart Actions
    cart_page_reusable.open_products_page()
    cart_page_reusable.add_products_to_cart(products)
    # Checkout Process
    cart_page_reusable.click_cart_element()
    checkout_page.click_on_proceed_to_checkout()
    checkout_page.click_on_place_order()
    checkout_page.card_info_actions(
        card["card_name"],
        card["card_number"],
        card["card_cvc"],
        card["card_expiry_month"],
        card["card_expiry_year"],
    )
    # Confirm payment and place the order
    checkout_page.click_pay_and_confirm_order()
    # Validation
    checkout_page.verify_order_confirmation_message("Order Placed!")
    # Clean up
    checkout_page.click_continue_btn()
    checkout_page.click_logout_link()


