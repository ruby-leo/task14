from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


class TestLoginFunction:
    # --- Positive Scenarios ---
    def test_input_fields_are_present(self, driver):
        login_page = LoginPage(driver)
        assert login_page.is_email_box_displayed() == True, "Email input box is missing!"
        assert login_page.is_password_box_displayed() == True, "Password input box is missing!"

    def test_sign_in_button_is_present(self, driver):
        login_page = LoginPage(driver)
        assert login_page.is_sign_in_button_displayed() == True, "Sign In button is not displayed!"

    def test_login_with_valid_email_and_password(self, driver, test_data):
        login_page = LoginPage(driver)
        login_page.enter_email(test_data["test_account_email"])
        login_page.enter_password(test_data["test_account_password"])
        login_page.click_sign_in()
        dashboard_page = DashboardPage(driver)
        assert "/dashboard" in dashboard_page.get_current_url(), "Login is not successful"

    # --- Negative Scenarios ---
    def test_login_with_valid_email_but_invalid_password(self, driver, test_data):
        login_page = LoginPage(driver)
        login_page.enter_email(test_data["test_account_email"])
        login_page.enter_password("IncorrectPassword")
        login_page.click_sign_in()
        assert login_page.is_invalid_password_error_message_displayed() == True, "Error message for invalid password is not displayed"

    def test_login_without_any_credentials(self, driver):
        login_page = LoginPage(driver)
        login_page.click_sign_in()
        assert login_page.is_missing_email_and_password_error_msg_displayed() == True, "Error message for missing email and password is not displayed"

    def test_login_with_valid_email_but_empty_password(self, driver, test_data):
        login_page = LoginPage(driver)
        login_page.enter_email(test_data["test_account_email"])
        login_page.enter_password("")  # Leaving field explicitly blank
        login_page.click_sign_in()
        assert login_page.is_password_required_error_msg_displayed() == True, "No error message is displayed for missing password"

    def test_login_with_invalid_email_format(self, driver):
        login_page = LoginPage(driver)
        login_page.enter_email("invalidEmailFormat")
        login_page.enter_password("AnyPassword123")
        login_page.click_sign_in()
        assert login_page.is_incorrect_email_error_msg_displayed() == True, "No error message about the incorrect email is displayed"