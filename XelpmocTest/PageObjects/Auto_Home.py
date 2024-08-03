from selenium.webdriver.common.by import By

from Utilitis.BaseClass import BaseClass


class Home(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    title_homepage = (By.TAG_NAME, 'h1')
    alert_btn = (By.XPATH, "//button[text()=' Your Sample Alert Button!']")

    def verify_app_title(self):
        title = self.return_text(self.title_homepage)
        assert title == "Your Website to practice Automation Testing"
