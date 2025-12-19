
from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    # Locators
        # self.CART_LINK = page.get_by_role("link", name="Cart") cart_page
        self.PROCEED_TO_CHECKOUT_BTN = page.get_by_text("Proceed To Checkout")
        self.PLACE_ORDER_BTN = page.get_by_role("link", name="Place Order")
        self.NAME_ON_CARD_INPUT = page.locator("input[name=\"name_on_card\"]")
        self.CARD_NUMBER_INPUT = page.locator("input[name=\"card_number\"]")
        self.CARD_CVC_INPUT = page.get_by_role("textbox", name="ex.")
        self.CARD_EXPIRY_MONTH_INPUT = page.get_by_role("textbox", name="MM")
        self.CARD_EXPIRY_YEAR_INPUT = page.get_by_role("textbox", name="YYYY")
        self.PAY_AND_CONFIRM_ORDER_BTN = page.get_by_role("button", name="Pay and Confirm Order")
        self.ORDER_CONFIRMATION_MESSAGE = page.get_by_text("Order Placed!")
        self.CONTINUE_BTN = page.get_by_role("link", name="Continue")
        self.LOGOUT_LINK = page.get_by_role("link", name="Logout")

    # Methods

    def click_on_proceed_to_checkout(self):
        self.PROCEED_TO_CHECKOUT_BTN.click()

    def click_on_place_order(self):
        self.PLACE_ORDER_BTN.click()

    def enter_name_on_card(self, name):
        self.NAME_ON_CARD_INPUT.fill(name)

    def enter_card_number(self, number):
        self.CARD_NUMBER_INPUT.fill(number)

    def enter_card_cvc_number(self, cvc):
        self.CARD_CVC_INPUT.fill(cvc)

    def enter_card_expiration_month(self, month):
        self.CARD_EXPIRY_MONTH_INPUT.fill(month)

    def enter_card_expiration_year(self, year):
        self.CARD_EXPIRY_YEAR_INPUT.fill(year)

    def card_info_actions(self, name, number, cvc, month, year):
        self.enter_name_on_card(name)
        self.enter_card_number(number)
        self.enter_card_cvc_number(cvc)
        self.enter_card_expiration_month(month)
        self.enter_card_expiration_year(year)

    def click_pay_and_confirm_order(self):
        self.PAY_AND_CONFIRM_ORDER_BTN.click()

    def verify_order_confirmation_message(self, message):
        expect(self.ORDER_CONFIRMATION_MESSAGE).to_contain_text(message)

    def click_continue_btn(self):
        self.CONTINUE_BTN.click()

    def click_logout_link(self):
        self.LOGOUT_LINK.click()

