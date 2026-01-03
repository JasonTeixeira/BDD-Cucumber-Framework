from behave import given, when, then


@given('I am on the login page')
def step_open_login(context):
    context.login_page.open(context.settings.base_url)


@when('I login with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.login_page.login(username, password)


@then('I should see the inventory page')
def step_inventory(context):
    context.inventory_page.assert_loaded()


@then('I should see an error containing "{message}"')
def step_error(context, message):
    context.login_page.assert_error_contains(message)
