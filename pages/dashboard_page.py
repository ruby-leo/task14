from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    profile_click_icon = (By.ID, "profile-click-icon")
    logout_link = (By.XPATH, "//div[text()='Log out']")
    new_alert_close_button = (By.CLASS_NAME, "custom-close-button")

    def click_profile_click_icon(self):
        self.click(self.profile_click_icon)

    def click_logout(self):
        self.click(self.logout_link)

    def get_current_url(self):
        return self.current_url("/dashboard")

    def is_new_alert_present(self):
        return self.is_displayed(self.new_alert_close_button)

    def click_new_alert_close_button(self):
        self.click(self.new_alert_close_button)