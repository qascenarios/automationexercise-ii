from playwright.sync_api import Page, expect


class RegisterPage:
    """
    Register Page
    Handles user signup and registration-related actions
    """

    def __init__(self, page: Page):
        self.page = page

    # Page Locators
        self.SIGNUP_SIGNIN_LINK = page.get_by_role("link", name=" Signup / Login")
        self.NAME_FIELD = page.get_by_role("textbox", name="Name")
        self.EMAIL_FIELD = (
            page.locator("form")
            .filter(has_text="Signup")
            .get_by_placeholder("Email Address")
        )
        self.SIGNUP_BTN = page.locator('button[data-qa="signup-button"]')
        self.DIALOG = page.get_by_role("button", name="Consent")
        self.REGISTER_SUCCESS_MSG = page.get_by_text("Account Created!")

    # Dialog Handling
    def accept_dialog(self):
        self.DIALOG.click()

    # Navigation Actions
    def click_signup_signin_link(self):
        self.SIGNUP_SIGNIN_LINK.click()

    # Signup Form Actions
    def input_name(self, name):
        self.NAME_FIELD.fill(name)

    def input_email(self, email):
        self.EMAIL_FIELD.fill(email)

    def click_signup_button(self):
        self.SIGNUP_BTN.click()

    # Registration Flow
    def register_actions(self, name, email):
        self.click_signup_signin_link()
        self.input_name(name)
        self.input_email(email)
        self.click_signup_button()

    # Registration Verification
    def verify_successful_registration(self, text):
        expect(self.REGISTER_SUCCESS_MSG).to_contain_text(text)
