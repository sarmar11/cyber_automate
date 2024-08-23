from behave import when, step

from pageobjects.login import LoginPageObject


@step('the user logs into PortSwigger')
def step_impl(context):
    LoginPageObject().open()
    LoginPageObject().login()


@when('the user logs out')
def step_impl(context):
    context.current_page = context.current_page.logout()

