from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "C:\\chrome-win64\\chrome.exe"
preferences = {
    "profile.default_content_settings.popups": 0,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
    "plugins.always_open_pdf_externally": True,
    "profile.default_content_setting_values.notifications": 1

}

# removeing info bar , "Chrome is being controlled by automated test software"
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument('--disable-notifications')
chrome_options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
driver.maximize_window()
