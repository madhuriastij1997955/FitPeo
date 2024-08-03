from selenium import webdriver
from Utilites import ConfigReader


def before_scenario(context, driver):
    browser = ConfigReader.get_browser()
    url = ConfigReader.get_url()
    if browser == "chrome":
        context.driver = webdriver.Chrome()
    elif browser == "firefox":
        context.driver = webdriver.Firefox()
    else:
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(url)


def after_scenario(context, driver):
    context.driver.close()
