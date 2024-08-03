import os
import time

import pytest
import allure
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



#
# driver = None
#
#
# @pytest.fixture(autouse=True)
# def take_screenshot(request):
#     yield
#     if request.node.rep_call.failed:
#         allure.attach(driver.get_screenshot_as_png(),
#                       name=request.function.__name__,
#                       attachment_type=allure.attachment_type.PNG)
#
#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", default="chrome")
#     parser.addoption("--env", default="UAT")
#
#
# @pytest.fixture(scope="class", autouse=True)
# def setUp(request):
#     global driver
#     browser = request.config.getoption("--browser")
#     # browser=crossbrowser
#     env = request.config.getoption("--env")
#
#     if browser == "chrome":
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.binary_location = "C:\\chrome-win64\\chrome.exe"
#         chrome_options.add_experimental_option("useAutomationExtension", False)
#         chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#         chrome_options.add_argument('--disable-notifications')
#         driver = webdriver.Chrome(options=chrome_options)
#         driver.maximize_window()
#         driver.get("http://a726c052c95f24c4b9a7ffb1f43a1e05-373855638.us-west-2.elb.amazonaws.com/login")
#     else:
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.binary_location = "C:\\chrome-win64\\chrome.exe"
#         chrome_options.add_experimental_option("useAutomationExtension", False)
#         chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#         chrome_options.add_argument('--disable-notifications')
#         driver = webdriver.Chrome(options=chrome_options)
#         driver.maximize_window()
#         driver.get("http://a726c052c95f24c4b9a7ffb1f43a1e05-373855638.us-west-2.elb.amazonaws.com/login")
#
#     request.cls.driver = driver
#
#     yield
#     driver.quit()

driver=webdriver.Chrome()
driver.get("https://www.google.com/")
links=driver.find_elements(By.TAG_NAME,"a")
for link in links:
    link.click()




