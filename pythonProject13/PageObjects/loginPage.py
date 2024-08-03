import time


from selenium.webdriver.common.by import By

from Utilities.Baseclass import Baseclass


class LoginPage(Baseclass):

    def __init__(self, driver):
        self.driver = driver

    username_txt_box = (By.ID, "normal_login_username")
    pwd_txt_box = (By.ID, "normal_login_password")
    login_btn = (By.XPATH, "//span[text()='Login']/parent::button")
    verify_btn=(By.XPATH,"//span[text()='Verify']/parent::button")
    logout_profile=(By.XPATH,"//div[@class='appbar-tools']/child::button")
    logout_btn=(By.XPATH,"//span[text()='Logout']")
    #########TP#########################
    tp_module=(By.XPATH,"//li[@modulename='TradingPartner']/descendant::span[text()='Trading Partner']")
    tp_add_btn=(By.XPATH,"//span[text()='Add Trading Partner']/parent::button")
    tp_txt_box=(By.ID,"tpName")
    tp_type_txt_box=(By.XPATH,"//span[text()='Select Trading Partner Type']")

    def login_to_app(self, uname, pwd):
        self.txt_send_keys(self.username_txt_box, uname)
        self.txt_send_keys(self.pwd_txt_box, pwd)
        self.javascript_click(self.login_btn)
        otp = "123456"
        for i in otp:
            xpath = (By.XPATH, "//input[@aria-label='Please enter OTP character " + str(i) + "']")
            self.txt_send_keys(xpath, i)
        self.javascript_click(self.verify_btn)

    def logout_to_app(self):
        time.sleep(10.0)
        self.move_to_elemt(self.logout_profile)
        self.javascript_click(self.logout_btn)

