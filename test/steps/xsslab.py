import time

from behave import given, when, then, step

from pageobjects.login import LoginPageObject
from pageobjects.xsslab import XSSLabPageObject


@given('I open XSS laboratory')
def step_impl(context):
    context.current_page = XSSLabPageObject()
    context.current_page.open()
    context.current_page.wait_until_loaded()


@when('I search the value "{value}"')
def step_impl(context, value):
    context.current_page.search_form(value)


@then('there are no alerts in browser')
def step_impl(context):
    time.sleep(1)
    is_visible = context.current_page.alert_visibility()
    assert not is_visible, 'Alert not expected'


@then('the filtered elements contain "{value}" value')
def step_impl(context, value):
    is_visible = context.current_page.alert_visibility()
    assert not is_visible, 'Alert not expected'
