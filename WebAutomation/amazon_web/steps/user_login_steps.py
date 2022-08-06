from behave import step
from nose.tools import assert_equals
from WebAutomation.amazon_web.pageObjects.user_login_objects import UserLoginObjects


userlogin_object = UserLoginObjects()


@step(u'I open amazon home page')
def open_home_page(context):
    userlogin_object.set_driver(context.browser, context.base_url)
    userlogin_object.open_home_page()


@step(u'I click on "{link}" link on the home page')
def click_on_the_link_on_home_page(context, link):
    userlogin_object.click_link_button(link)


@step(u"I should see signin screen is shown with title '{title}'")
def i_should_see_sign_in_screen_is_shown(context, title):
    assert_equals(title, userlogin_object.verify_signin_screen_title())


@step(u'I should see following fields shown on signin screen')
def i_should_see_following_fields_shown_on_signin_screen(context):
    for row in context.table:
        for expect_label, exp_value in row.as_dict().items():
            label, value = userlogin_object.get_signin_fields_detail(expect_label)
            assert_equals(label, expect_label)
            assert_equals(value, exp_value)


@step(u'I should see "{button}" button is shown under email field of signin screen')
def i_should_see_button_is_shown_under_email_field_of_signin_screen(context, button):
    assert_equals(button, userlogin_object.verify_signin_screen_button())


@step(u'I click on "{button}" button on signin screen')
def i_click_on_button_on_signin_screen(context, button):
    userlogin_object.click_signin_screen_button(button)


@step(u'I should see following errors under fields on signin screen')
def i_should_see_following_errors_under_fields_on_singin_screen(context):
    for row in context.table:
        for label, exp_value in row.as_dict().items():
            assert_equals(exp_value, userlogin_object.verify_signin_fields_errors(label))


@step(u'I fill in the following details on signin screen')
def i_fill_in_the_following_details_on_signin_screen(context):
    for row in context.table:
        for label, value in row.as_dict().items():
            userlogin_object.fill_in_fields(label, value)


@step(u'I should see following errors on signin screen')
def i_should_see_following_erros_on_singin_screen(context):
    for row in context.table:
        for label, value in row.as_dict().items():
            assert_equals(value, userlogin_object.verify_signin_errors(label))


@step(u'I should see "{button}" button is shown at the bottom of signin screen')
def i_should_see_button_is_shown_at_the_bottom_of_signin_screen(context, button):
    assert_equals(button, userlogin_object.verify_create_amazon_button())