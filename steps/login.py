from assertpy import assert_that

from behave import given, then, when

import page_objects.login_page as login_page


@given("I am on log in page")
def step_impl(context):
    context.page = login_page.LoginPage(context.driver)


@when("I fill email field with correct data")
def step_impl(context):
    context.page.email_field.get_when_visible().send_keys(context.page.user_email)


@when("I fill password field with correct data")
def step_impl(context):
    context.page.password_field.get_when_visible().send_keys(context.page.user_password)


@when("I click on 'Zaloguj sie' button")
def step_impl(context):
    context.page.login_button.get_when_clickable().click()


@then("I am redirected to my account page")
def step_impl(context):
    (assert_that(context.page.account_name.get_when_visible().text)
     .described_as("Check if redirected to account page")
     .contains(context.page.user_name))


@then("I see information that password field is empty")
def step_impl(context):
    (assert_that(context.page.empty_password_error.get_when_visible()[1].text)
     .described_as("Checking correctness of information")
     .contains("Pole hasła jest puste. Wypełnij je."))
