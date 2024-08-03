from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class Baseclass:
    def txt_send_keys(self, locator, txt):
        exp_wait = WebDriverWait(self.driver, 15, 5)
        web_ele = exp_wait.until(EC.visibility_of_element_located(locator))
        web_ele.clear()
        self.driver.execute_script("arguments[0].value=''", web_ele)
        web_ele.send_keys(txt)

    def click_btn(self, locator):
        exp_wait = WebDriverWait(self.driver, 15, 5)
        web_ele = exp_wait.until(EC.visibility_of_element_located(locator))
        web_ele.click()

    def javascript_click(self,locator):
        exp_wait = WebDriverWait(self.driver, 15, 5)
        web_ele = exp_wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();",web_ele)


    def move_to_elemt(self,locator):
        exp_wait = WebDriverWait(self.driver, 15, 5)
        web_ele = exp_wait.until(EC.visibility_of_element_located(locator))
        mouse_act=ActionChains(self.driver)
        mouse_act.move_to_element(web_ele).perform()


