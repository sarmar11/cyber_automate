import time

from behave import given, when, then

from pageobjects.sqlilab import SQLiLabPageObject


@given('I open SQLi laboratory')
def step_impl(context):
    context.current_page = SQLiLabPageObject()
    context.current_page.open()
    context.current_page.wait_until_loaded()


@when('add a filter to url "{value}"')
def step_impl(context, value):
    context.visible_titles_ini = len(context.current_page.list_titles)
    context.current_page.force_url_sqli(value)


@then('I check visible data contains allowed values')
def step_impl(context):
    context.visible_titles_end = len(context.current_page.list_titles)
    assert context.visible_titles_end <= context.visible_titles_ini, 'SQLi attack happened'
