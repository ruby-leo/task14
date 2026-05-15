from pages import dashboard_page
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

class TestLogoutFunction:
    def test_if_logout_is_working(self, driver, test_data):
        login_page = LoginPage(driver)
        login_page.perform_login(test_data["test_account_email"], test_data["test_account_password"])
        dashboard_page = DashboardPage(driver)
        if(dashboard_page.is_new_alert_present()):
            dashboard_page.click_new_alert_close_button()
        dashboard_page.click_profile_click_icon()
        dashboard_page.click_logout()
        assert "/login" in login_page.get_current_url()