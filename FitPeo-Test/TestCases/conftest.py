import os

import pytest
from selenium import webdriver


@pytest.fixture(autouse=True, scope="class")
def setUp(request):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument('--disable-notifications')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(3.2)
    driver.get("https://www.fitpeo.com/home")
    request.cls.driver = driver
    yield
    driver.quit()




