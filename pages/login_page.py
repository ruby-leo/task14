from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    email_text_box = (By.XPATH, "//input[contains(normalize-space(@placeholder),'Enter your mail')]")
    password_text_box = (By.XPATH, "//input[contains(normalize-space(@placeholder),'Enter your password')]")
    sign_in_button = (By.CLASS_NAME, "primary-btn")
    invalid_password_error_msg = (By.XPATH, "//p[text()='*Incorrect password!']")

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



