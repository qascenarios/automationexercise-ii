from playwright.sync_api import Page
from pages.search_product_page import SearchProductsPage

class CartPage:
    """
    CartPage class encapsulates all interactions with the shopping cart page
    of the e-commerce website. It handles:
    - Navigating to the Products page
    - Searching for products
    - Adding products to the cart
    - Clearing search fields
    - Verifying that products are correctly added to the cart

    This follows the Page Object Model pattern to keep tests clean and reusable.
    """

    def __init__(self, page: Page):
        self.page = page

    # Locators
        self.PRODUCTS_LINK = page.get_by_role("link", name=" Products")
        self.SEARCH_INPUT = page.get_by_role("textbox", name="Search Product")
        self.SEARCH_BUTTON = page.locator("#submit_search")
        self.ADD_TO_CART_BUTTONS = page.get_by_text("Add to cart")
        self.CONTINUE_SHOPPING_BUTTON = page.get_by_role(
            "button", name="Continue Shopping"
        )
        self.PRODUCT_NAMES_IN_CART = page.locator(
            "td.cart_description h4 a"
        )
        self.CART_LINK = page.get_by_role("link", name="Cart")

    # Methods

    # Navigation
    def open_products_page(self):
        self.PRODUCTS_LINK.click()

    # Search Actions
    def search_for_product(self, product: str):
        self.SEARCH_INPUT.fill(product)
        self.SEARCH_BUTTON.click()

    def clear_search_field(self):
        self.SEARCH_INPUT.clear()

    # Cart Actions
    def add_first_search_result_to_cart(self):
        self.ADD_TO_CART_BUTTONS.first.click()
        self.CONTINUE_SHOPPING_BUTTON.click()

    def add_products_to_cart(self, products):
        for product in products:
            self.search_for_product(product)
            self.add_first_search_result_to_cart()
            self.clear_search_field()

    def click_cart_element(self):
        self.CART_LINK.click()

    # Verification
    def assert_products_in_cart(self, expected_products):
        self.click_cart_element()
        cart_product_names = self.PRODUCT_NAMES_IN_CART.all_text_contents()

        for product in expected_products:
            assert product in cart_product_names, (
                f"Expected product '{product}' not found in cart. "
                f"Actual products: {cart_product_names}"
            )



