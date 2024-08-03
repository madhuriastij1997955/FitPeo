import logging
import random
import string
import time
from datetime import datetime


from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Baseclass:

    def verify_element_displayed(self, locator):
        exp_wait = WebDriverWait(self.driver, 5, 1, Exception)
        web_ele = exp_wait.until(EC.presence_of_element_located(locator))
        status = web_ele.is_displayed()
        return status

    def send_keys(self, locator, text):
        exp_wait = WebDriverWait(self.driver, 5, 1)
        web_ele = exp_wait.until(EC.visibility_of_element_located(locator))

        web_ele.clear()
        web_ele.send_keys(Keys.CONTROL + 'a')
        web_ele.send_keys(Keys.DELETE)
        self.driver.execute_script("arguments[0].value ='';", web_ele)
        web_ele.send_keys(text)

    def click_element(self, locator):
        exp_wait = WebDriverWait(self.driver, 25, 1)
        web_ele = exp_wait.until(EC.presence_of_element_located(locator))
        web_ele.click()

    def return_text(self, locator):
        exp_wait = WebDriverWait(self.driver, 85, 1)
        web_ele = exp_wait.until(EC.visibility_of_element_located(locator))
        return web_ele.text

    def get_txt_box_value(self, locator, attirubute):
        exp_wait = WebDriverWait(self.driver, 25, 1)
        web_ele = exp_wait.until(EC.presence_of_element_located(locator))
        # exp_wait.until(EC.staleness_of(web_ele))
        return web_ele.get_attribute(attirubute)



    def move_to_element(self, locator):
        mouse_act = ActionChains(self.driver)
        exp_wait = WebDriverWait(self.driver, 25, 1)
        web_ele = exp_wait.until(EC.presence_of_element_located(locator))
        time.sleep(0.5)
        mouse_act.move_to_element(web_ele).perform()



    def move_to_element_horizantal_offset(self, locator,value):
        mouse_act = ActionChains(self.driver)
        exp_wait = WebDriverWait(self.driver, 25, 1)
        web_ele = self.driver.find_element(locator[0],locator[1])
        time.sleep(0.5)
        mouse_act.click_and_hold(web_ele).move_by_offset(value,0).release(web_ele).perform()

    def click_and_hold(self, locator):
        mouse_act = ActionChains(self.driver)
        exp_wait = WebDriverWait(self.driver, 25, 1)
        web_ele = exp_wait.until(EC.presence_of_element_located(locator))
        time.sleep(0.5)
        mouse_act.click_and_hold(web_ele).perform()

    def javascripit_click(self, locator):
        exp_wait = WebDriverWait(self.driver, 5, 1)
        web_ele = exp_wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", web_ele)





    def is_enabled(self, locator):
        ele = self.driver.find_element(locator[0], locator[1])
        return ele.is_enabled()
    def is_displayed(self, locator):
        ele = self.driver.find_element(locator[0], locator[1])
        return ele.is_displayed()

    def get_time_stamp(self):
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return current_datetime

    def find_elements(self, locator):
        return self.driver.find_elements(locator[0], locator[1])

    def scroll_to_ele(self,locator):
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(locator[0], locator[1] ))

    def get_tag_attribute(self, locator, attirubute):
        get_value = self.driver.find_element(locator[0], locator[1]).get_attribute(attirubute)
        return get_value




