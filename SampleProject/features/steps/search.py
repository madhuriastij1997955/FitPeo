import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


# @given('launch the browser and navigate to home page1')
# def step_impl(context):
#     context.driver = webdriver.Chrome()
#     context.driver.maximize_window()
#     context.driver.get("https://tutorialsninja.com/demo/")


@when('Enter valid product in search box')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("HP")


@when('Click on search box')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()


@then('Validate product should get displayed in search results')
def step_impl(context):
    time.sleep(5.0)
    assert context.driver.find_element(By.XPATH, "//a[text()='HP LP3065']").is_displayed()


@when('Enter Invalid product in search box')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("HP123")


@when('Do not search product in search box')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys(" ")


@then('Validate Proper message is displayed in search results')
def step_impl(context):
    time.sleep(3.0)
    txt = context.driver.find_element(By.XPATH, "//p[text()='There is no product that matches the search criteria.']").text
    assert txt == "There is no product that matches the search criteria."




