import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = None



def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--env", default="UAT")


@pytest.fixture(scope="class", autouse=True)
def Set_up(request):
    global driver
    browser = request.config.getoption("--browser")
    # browser=crossbrowser
    env = request.config.getoption("--env")
    if browser == "chrome":
        print(browser + " is started")
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(time_to_wait=5.0)
    else:
        print("chrome is started")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = "C:\\old data\\chrome-win64\\chrome.exe"

        driver = webdriver.Chrome(options=chrome_options, service=Service("C:\\Users\\Madhuri.Jasti\\PycharmProjects"
                                                                          "\\FATBaseVersion\\venv\\Scripts\\chromedriver.exe"))
        driver.maximize_window()
        driver.implicitly_wait(time_to_wait=5.0)
