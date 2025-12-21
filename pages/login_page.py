from playwright.sync_api import Page, expect

class LoginPage:
    """
    Login Page
    Handles user authentication and login validation
    """

    def __init__(self, page: Page):
        self.page = page

        # Page Locators
        self.LOGIN_EMAIL_FIELD = (
            page.locator("form")
            .filter(has_text="Login")
            .get_by_placeholder("Email Address")
        )
        self.LOGIN_PASSWORD_FIELD = page.get_by_role("textbox", name="Password")
        self.LOGIN_BUTTON = page.get_by_role("button", name="Login")
        self.SUCCESSFUL_LOGIN_VALIDATION = page.get_by_role("link", name="Logout")
        self.FAILED_LOGIN_VALIDATION = page.get_by_text("Your email or password is incorrect")

    # Login Form Actions
    def fill_email_address(self, email):
        self.LOGIN_EMAIL_FIELD.fill(email)

    def fill_password(self, password):
        self.LOGIN_PASSWORD_FIELD.fill(password)

    def submit_login(self):
        self.LOGIN_BUTTON.click()

    # Login Verification
    def verify_successful_login(self):
        expect(self.SUCCESSFUL_LOGIN_VALIDATION).to_be_visible()

    def verify_failed_login(self):
        expect(self.FAILED_LOGIN_VALIDATION).to_be_visible()

    # Login Flow
    def login_actions(self, email, password):
        self.fill_email_address(email)
        self.fill_password(password)
        self.submit_login()
