from behave import *


@When('I login successfully with "{username}" and "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)


@Then("There are 6 products on the Inventory page")
def step_impl(context):
    assert context.inventory_page.get_products_count() == 6
