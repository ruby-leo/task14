from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    email_text_box = (By.XPATH, "//input[contains(normalize-space(@placeholder),'Enter your mail')]")
    password_text_box = (By.XPATH, "//input[contains(normalize-space(@placeholder),'Enter your password')]")
    sign_in_button = (By.CLASS_NAME, "primary-btn")
    invalid_password_error_msg = (By.XPATH, "//p[text()='*Incorrect password!']")
    missing_email_and_pw_error_msg = (By.XPATH, "//p[text()='Email and password required!']")
    password_required_error_msg = (By.XPATH, "//p[text()='Password required!']")
    incorrect_email_error_msg = (By.XPATH, "//p[text()='*Incorrect email!']")

    def enter_email(self, email_address):
        self.enter_text(self.email_text_box, email_address)

    def enter_password(self, password):
        self.enter_text(self.password_text_box, password)

    def click_sign_in(self):
        self.click(self.sign_in_button)

    def is_invalid_password_error_message_displayed(self):
        return self.is_displayed(self.invalid_password_error_msg)

    def perform_login(self, email_address, password):
        self.enter_text(self.email_text_box, email_address)
        self.enter_text(self.password_text_box, password)
        self.click(self.sign_in_button)

    def get_current_url(self):
        return self.current_url("/login")

    def is_email_box_displayed(self):
        return self.is_displayed(self.email_text_box)

    def is_password_box_displayed(self):
        return self.is_displayed(self.password_text_box)

    def is_sign_in_button_displayed(self):
        return self.is_displayed(self.sign_in_button)

    def is_missing_email_and_password_error_msg_displayed(self):
        return self.is_displayed(self.missing_email_and_pw_error_msg)

    def is_password_required_error_msg_displayed(self):
        return self.is_displayed(self.password_required_error_msg)

    def is_incorrect_email_error_msg_displayed(self):
        return self.is_displayed(self.incorrect_email_error_msg)