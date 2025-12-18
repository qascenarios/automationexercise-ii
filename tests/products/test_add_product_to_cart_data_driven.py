import time

import pytest
from utils.helpers import read_json
from playwright.sync_api import Page, expect
from pages.search_product_page import SearchProductsPage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from utils.config import LoginCredentials
from pages.cart_page import CartPage
from conftest import open_browser


# Test Data
products = read_json("testdata/products.json")["products"]

def test_search_product(open_browser: Page):

    # Page Object Initialization
    register_page = RegisterPage(open_browser)
    login_page = LoginPage(open_browser)
    cart_page = CartPage(open_browser)

    # Precondition Handling
    register_page.accept_dialog()

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



