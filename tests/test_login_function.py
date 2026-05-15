from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

class TestLoginFunction:
    def test_login_with_valid_email_and_password(self, driver, test_data):
        login_page = LoginPage(driver)
        login_page.enter_email(test_data["test_account_email"])
        login_page.enter_password(test_data["test_account_password"])
        login_page.click_sign_in()

        dashboard_page = DashboardPage(driver)
        assert "/dashboard" in dashboard_page.get_current_url()

    def test_login_with_valid_email_but_invalid_password(self, driver, test_data):
        login_page = LoginPage(driver)
        login_page.enter_email(test_data["test_account_email"])
        login_page.enter_password("IncorrectPassword")
        login_page.click_sign_in()

        assert login_page.is_invalid_password_error_message_displayed() == True