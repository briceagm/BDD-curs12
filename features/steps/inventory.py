from behave import *


@When('I login successfully with "{username}" and "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)


@Then("There are 6 products on the Inventory page")
def step_impl(context):
    assert context.inventory_page.get_products_count() == 6


@Given('I am not log in user')
def step_impl(context):
    pass


@When('I go to the Inventory Page')
def step_impl(context):
    context.inventory_page.get_page()


@Then('I am redirected to Login Page')
def step_impl(context):
    assert context.browser.get_current_url() == context.login_page.URL


@Then('I receive a Sad Face message')
def step_impl(context):
    expected_error_message = "Epic sadface: You can only access '/inventory.html' when you are logged in."
    assert context.login_page.get_error_message() == expected_error_message

