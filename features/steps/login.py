from behave import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

@given('we visit login page')
def step_impl(context):
	context.browser = webdriver.Chrome()
	context.browser.implicitly_wait(10)
	context.browser.get('http://store.demoqa.com/products-page/your-account/')
	context.user_field = context.browser.find_element_by_name("log")
	context.password_field = context.browser.find_element_by_name("pwd")
	context.login_button = context.browser.find_element_by_name("submit")

@when('we enter an username "{user}" and a password "{password}"')
def step_impl(context, user, password):
	if user == "N/A":
		user = ""
	if password == "N/A":
		password = ""
	context.user = user
	context.password = password
	context.user_field.send_keys(user)
	context.password_field.send_keys(password)
	context.login_button.click()

@then('we receive an error message "{error}"')
def step_impl(context, error):
	WebDriverWait(context.browser, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "response"), error))
	context.response = context.browser.find_element_by_class_name("response")
	response = context.response.text
	assert error in response
	context.browser.close()

@then('we are redirected to the main page')
def step_impl(context):
	#time.sleep(3)
	#greet = context.browser.find_element_by_link_text("Howdy, " + context.user)
	greet = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Howdy, " + context.user)))
	greet = greet.text
	assert greet == "Howdy, " + context.user
	logout = context.browser.find_element_by_link_text("(Logout)")
	logout.click()
	context.browser.close()
