
from playwright.sync_api import Page, expect

class DeletePage:
    def __init__(self, page: Page):
        self.page = page
        # Locator for all delete buttons in the cart
        self.DELETE_PRODUCT_BUTTONS = page.locator(".cart_quantity_delete")
        # Locator for all product names in the cart
        self.PRODUCT_NAMES = page.locator("td.cart_description h4 a")


    # Actions

    def delete_product_from_cart(self, product_names):
        """
            Delete products from the cart by their names.
            :param product_names: List of product names to delete
        """
        for name_to_delete in product_names:
            cart_products = self.PRODUCT_NAMES.all_text_contents()

            if name_to_delete not in cart_products:
                print(f"Product not found in cart: {name_to_delete}")
                continue

            index = cart_products.index(name_to_delete)

            self.DELETE_PRODUCT_BUTTONS.nth(index).click()
            self.DELETE_PRODUCT_BUTTONS.nth(index).wait_for(state="attached")



