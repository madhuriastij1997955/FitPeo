import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


@Given('launch the browser and navigate to home page')
def step_impl(context):
    # context.driver = webdriver.Chrome()
    # context.driver.maximize_window()
    # context.driver.get("https://tutorialsninja.com/demo/")
    time.sleep(2.0)
    mouse_act = ActionChains(context.driver)
    mouse_act.move_to_element(context.driver.find_element(By.XPATH, "//span[text()='My Account']")).click().perform()
    context.driver.find_element(By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']/descendant::a[text("
                                          ")='Login']").click()


@when(u'Login to Application with valid username and password')
def step_impl(context):
    pass


@when(u'click on login button')
def step_impl(context):
    pass


@then(u'I should get logged in')
def step_impl(context):
   pass


@when(u'Enter valid Invalid username and valid password')
def step_impl(context):
    pass


@then(u'Verify proper message is displayed for login page')
def step_impl(context):
    pass


@when(u'Enter valid username and Invalid password')
def step_impl(context):
   pass


@when(u'Don\'t enter username and passowrd')
def step_impl(context):
    pass
