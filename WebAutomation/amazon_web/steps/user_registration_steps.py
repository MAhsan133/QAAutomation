from behave import step
from nose.tools import assert_equals
from WebAutomation.amazon_web.pageObjects.user_registration_objects import UserRegistrationObjects


register_object = UserRegistrationObjects()


@step(u"I should see registration screen is shown with title '{title}'")
def i_should_see_registration_screen_is_shown(context, title):
    register_object.set_driver(context.browser, context.base_url)
    assert_equals(title, register_object.verify_registration_screen())


@step(u'I should see following fields shown on create account screen')
def click_on_sign_up_button_on_login_page(context):
    expected_dict = {}
    for row in context.table:
        for expect_label, exp_value in row.as_dict().items():
            expected_dict[expect_label] = exp_value
    fields_dict = register_object.get_create_account_fields()
    assert_equals(expected_dict, fields_dict)


@step(u'I should see "{button}" button is shown at the bottom of screen')
def i_can_see_popup_window_is_shown_with_title_on_create_user_screen(context, button):
    assert_equals(button, register_object.verify_signup_screen_button())


@step(u'I click on "{button}" button on create account screen')
def i_can_see_following_buttons_with_detail_on_popup_window(context, button):
    register_object.click_signup_screen_button(button)


@step(u'I should see following errors under fields on create account screen')
def i_click_on_button_on_popup_window(context):
    for row in context.table:
        for label, value in row.as_dict().items():
            if value:
                assert_equals(value, register_object.verify_signup_field_errors(label))


@step(u'I fill in the following details on create account screen')
def i_fill_in_the_following_details_on_create_account_screen(context):
    for row in context.table:
        for field, value in row.as_dict().items():
            register_object.fill_in_the_field(field, value)


@step(u'I should see following invalid field errors on create account screen')
def i_should_see_following_invalid_field_errors_on_create_account_screen(context):
    for row in context.table:
        for label, value in row.as_dict().items():
            if value:
                assert_equals(value, register_object.verify_invalid_field_errors(label))


@step(u'I can see solve puzzle screen with title "{title}"')
def i_can_see_puzzle_on_screen(context, title):
    assert_equals(title, register_object.verify_puzzle_screen_shown())