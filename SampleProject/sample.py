import time

from  webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

chrome_options=webdriver.ChromeOptions()
chrome_options.binary_location="C:\\chrome-win64\\chrome.exe"
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument('--disable-notifications')


# driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
driver=webdriver.Chrome(options=chrome_options)
driver.maximize_window()
time.sleep(5.0)
