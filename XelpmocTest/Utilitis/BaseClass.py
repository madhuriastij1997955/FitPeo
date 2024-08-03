from selenium.webdriver.support.wait import WebDriverWait
import logging
import random
import string
import time
from datetime import datetime


from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:

    def return_text(self, locator):
        exp_wait = WebDriverWait(self.driver, 85, 1)
        web_ele = exp_wait.until(EC.visibility_of_element_located(locator))
        return web_ele.text