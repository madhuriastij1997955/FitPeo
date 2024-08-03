from behave import *
import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
from PageObjects.Registration import Registration


@given('Launch the browser and navigate to registration page')
def step_impl(context):
    # context.driver = webdriver.Chrome()
    # context.driver.maximize_window()
    #
    # context.driver.get("https://tutorialsninja.com/demo/")

    # context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    # mouse_act.move_to_element(context.driver.find_element(By.XPATH, "//li[@class='dropdown open']/descendant::li/a["
    #                                                                 "text()='Register']")).perform()
    #
    # context.driver.find_element(By.XPATH, "//li[@class='dropdown open']/descendant::li/a[text()='Register']").click()
    reg = Registration(context.driver)
    reg.navigate_to_registarionPage()


@when('Enter all manadatory fields')
def step_impl(context):
    fake_data = Faker()
    context.mailid = fake_data.email()

    context.driver.find_element(By.ID, "input-firstname").send_keys(fake_data.name())
    context.driver.find_element(By.ID, "input-lastname").send_keys(fake_data.name())
    context.driver.find_element(By.ID, "input-email").send_keys(context.mailid)
    context.driver.find_element(By.ID, "input-telephone").send_keys(fake_data.phone_number())
    pwd = fake_data.text(20)
    context.driver.find_element(By.ID, "input-password").send_keys(pwd)
    context.driver.find_element(By.ID, "input-confirm").send_keys(pwd)
    context.driver.find_element(By.NAME, "agree").click()


@when('Click on continue button')
def step_impl(context):
    print("not clicked")
    context.driver.find_element(By.XPATH, "//input[@value='Continue']").click()


@then('Account should be created')
def step_impl(context):
    txt = context.driver.find_element(By.XPATH,
                                      "//h1[text()='Your Account Has Been Created!']").text

    assert txt == "Your Account Has Been Created!"


@when('Enter all manadatory fields except mailid')
def step_impl(context):
    fake_data = Faker()
    context.driver.find_element(By.ID, "input-firstname").send_keys(fake_data.name())
    context.driver.find_element(By.ID, "input-lastname").send_keys(fake_data.name())
    context.driver.find_element(By.ID, "input-email").send_keys("")
    context.driver.find_element(By.ID, "input-telephone").send_keys(fake_data.phone_number())
    pwd = fake_data.text(20)
    context.driver.find_element(By.ID, "input-password").send_keys(pwd)
    context.driver.find_element(By.ID, "input-confirm").send_keys(pwd)


@when('Enter exsiting mailid')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("madhuri.jasti1997@gmail.com")

    context.driver.find_element(By.NAME, "agree").click()


@then('Account should not be created and error message should be displayed')
def step_impl(context):
    txt = context.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text
    print(txt)
    assert txt.__contains__("Warning: E-Mail Address is already registered!")


@when('Do not enter values in registartion page')
def step_impl(context):
    pass
    # context.driver.find_element(By.CLASS_NAME, "btn btn-primary").click()

# @then(u'Proper warning message should be displayed for all mandatory fields')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Proper warning message should be displayed for all mandatory fields')
