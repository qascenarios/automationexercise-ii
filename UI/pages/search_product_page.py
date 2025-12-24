from playwright.sync_api import Page


class SearchProductsPage:
    """
    Search Products Page
    Handles product search and search result validation
    """

    def __init__(self, page: Page):
        self.page = page

        # Page Locators
        self.SEARCH_PRODUCTS_ELEMENT = page.get_by_role("link", name=" Products")
        self.SEARCH_BOX_FIELD = page.get_by_role("textbox", name="Search Product")
        self.SEARCH_BUTTON = page.locator("#submit_search")
        self.PRODUCT_NAMES = page.locator("div.single-products div.productinfo p")

    # Navigation Actions
    def click_product_element(self):
        self.SEARCH_PRODUCTS_ELEMENT.click()
        self.page.wait_for_load_state("networkidle")

    # Search Actions
    def search_for_product(self, item):
        self.SEARCH_BOX_FIELD.fill(item)

    def click_on_search_btn(self):
        self.SEARCH_BUTTON.click()

    def clear_search_field(self):
        self.SEARCH_BOX_FIELD.clear()

    # Search Result Validation
    def get_first_searched_product(self):
        return self.PRODUCT_NAMES.first
