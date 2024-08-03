from selenium.webdriver.common.by import By

from Utilites.Baseclass import Baseclass


class Registration(Baseclass):

    def __init__(self, driver):
        self.driver = driver

    account_ele = (By.XPATH, "//span[text()='My Account']")
    regi_ele=(By.XPATH,"//li[@class='dropdown open']/descendant::li/a[text()='Register']")

    def navigate_to_registarionPage(self):
        self.click_element(self.account_ele)
        self.move_to_element(self.regi_ele)
        self.click_element(self.regi_ele)

