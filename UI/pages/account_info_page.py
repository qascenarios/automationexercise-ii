from playwright.sync_api import Page


class AccountInformationPage:
    """
    Account Information Page
    Handles user account details input and account creation actions
    """

    def __init__(self, page: Page):
        self.page = page

        # Page Locators
        self.PASSWORD_FIELD = page.locator("#password")
        self.FIRST_NAME = page.locator("#first_name")
        self.LAST_NAME = page.locator("#last_name")
        self.ADDRESS1_FIELD = page.locator("#address1")
        self.COUNTRY_FIELD = page.locator("#country")
        self.STATE_FIELD = page.locator("#state")
        self.CITY_FIELD = page.locator("#city")
        self.ZIPCODE_FIELD = page.locator("#zipcode")
        self.MOBILE_NUM_FIELD = page.locator("#mobile_number")
        self.CREATE_ACCOUNT_BTN = page.locator('button[data-qa="create-account"]')

    # Field Input Actions
    def input_password(self, password):
        self.PASSWORD_FIELD.fill(password)

    def input_firstname(self, firstname):
        self.FIRST_NAME.fill(firstname)

    def input_lastname(self, lastname):
        self.LAST_NAME.fill(lastname)

    def input_address1(self, address1):
        self.ADDRESS1_FIELD.fill(address1)

    def select_country(self, country):
        self.COUNTRY_FIELD.select_option(label=country)

    def input_state(self, state):
        self.STATE_FIELD.fill(state)

    def input_city(self, city):
        self.CITY_FIELD.fill(city)

    def input_zipcode(self, zipcode):
        self.ZIPCODE_FIELD.fill(zipcode)

    def input_mobile_number(self, phone):
        self.MOBILE_NUM_FIELD.fill(phone)

    # Form Submission
    def click_create_acct_btn(self):
        self.CREATE_ACCOUNT_BTN.click()

    # Account Creation Flow
    def account_info_actions(
        self,
        password,
        firstname,
        lastname,
        address1,
        country,
        state,
        city,
        zipcode,
        phone
    ):
        self.input_password(password)
        self.input_firstname(firstname)
        self.input_lastname(lastname)
        self.input_address1(address1)
        self.select_country(country)
        self.input_state(state)
        self.input_city(city)
        self.input_zipcode(zipcode)
        self.input_mobile_number(phone)
        self.click_create_acct_btn()
