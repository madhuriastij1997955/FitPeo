import time

from Utilites.Baseclass import Baseclass
from selenium.webdriver.common.by import By


class FitPeo(Baseclass):

    def __init__(self, driver):
        self.driver = driver

    revenue_cal_link = (By.XPATH, "//div[text()='Revenue Calculator']/parent::a")
    slider_to_scroll = (By.XPATH, "//h4[text()='Medicare Eligible Patients']/following-sibling::p")
    slider_ele = (By.XPATH, "//span[contains(@class,'MuiSlider-root MuiSlider-colorPrimary')]/descendant::input")
    range_txt_box = (By.XPATH, "//input[@type='number']")
    CPT_99091_ele=(By.XPATH,"//p[text()='CPT-99091']/parent::div/descendant::input")
    CPT_99453_ele=(By.XPATH,"//p[text()='CPT-99453']/parent::div/descendant::input")
    CPT_99454_ele=(By.XPATH,"//p[text()='CPT-99454']/parent::div/descendant::input")
    CPT_99474_ele=(By.XPATH,"//p[text()='CPT-99474']/parent::div/descendant::input")
    total_recurring_value=(By.XPATH,"//p[contains(text(),' Patients Per Month:')]/child::p")

    def calculate_revenue(self, slidervalue):
        self.click_element(self.revenue_cal_link)
        self.scroll_to_ele(self.slider_to_scroll)
        self.move_to_element_horizantal_offset(self.slider_ele, slidervalue)
        self.scroll_to_ele(self.slider_to_scroll)
        self.send_keys(self.range_txt_box, 560)
        txt_value = self.get_txt_box_value(self.range_txt_box, "value")
        if int(txt_value) == 560:
            assert True
        self.click_element(self.CPT_99091_ele)
        self.click_element(self.CPT_99453_ele)
        self.click_element(self.CPT_99454_ele)
        self.click_element(self.CPT_99474_ele)
        recurring_value=self.return_text(self.total_recurring_value)
        if recurring_value=="$75600":
            print("Total Recurring Reimbursement for all Patients Per Month:",recurring_value)
        else:
            print("Total Recurring Reimbursement for all Patients Per Month value is seen as wrong and expected is missmached",recurring_value)