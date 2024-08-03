import time

from Utilities.readProperties import Read_login_details
from PageObjects.loginPage import LoginPage

class Test_Login_page:
    uname = Read_login_details().get_username()
    pwd = Read_login_details().get_password()

    def test_login_to_app(self):
        lp=LoginPage(self.driver)
        lp.login_to_app(self.uname,self.pwd)
        lp.logout_to_app()


