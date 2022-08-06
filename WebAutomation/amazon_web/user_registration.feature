Feature: User Registration

  Scenario: 1 Verify create account screen detail
    Given I open amazon home page
    Then I click on "Start here" link on the home page
    And I should see registration screen is shown with title 'Create account'
    Then I should see following fields shown on create account screen
      | Your name           | Mobile number or email | Password               | Re-enter password |
      | First and last name |                        | At least 6 characters  |                   |
    And I should see "Continue" button is shown at the bottom of screen
    When I click on "Continue" button on create account screen
    Then I should see following errors under fields on create account screen
      | Your name           | Mobile number or email                    | Password                        |
      | Enter your name     | Enter your email or mobile phone number   |  Minimum 6 characters required  |

  Scenario Outline: 2 Verify Mandatory field error on each field
    Given I fill in the following details on create account screen
      | Your name           | Mobile number or email | Password               | Re-enter password   |
      | <your_name>         | <mobile_email>         | <password>             | <re_enter_password> |
    Then I click on "<button>" button on create account screen
    And I should see following errors under fields on create account screen
      | Your name             | Mobile number or email                    | Password                        | Re-enter password     |
      | <your_name_error>     | <mobile_email_error>                      | <password_error>                | <re_enter_pass_error> |
    Examples:
      | your_name   | mobile_email              | password  | re_enter_password | your_name_error   | mobile_email_error                       | password_error                 | re_enter_pass_error     | button       |
      |             | paul.serice101@gmail.com  | 123456    | 123456            | Enter your name   |                                          |                                |                         | Verify email |
      | abcd        |                           | 123456    | 123456            |                   |  Enter your email or mobile phone number |                                |                         | Continue     |
      | abcd        | paul.serice101@gmail.com  |           |                   |                   |                                          |  Minimum 6 characters required |                         | Verify email |
      | abcd        | paul.serice101@gmail.com  | 123456    |                   |                   |                                          |                                | Type your password again| Verify email |

  Scenario Outline: 3 Validate invalid field error on each field
    Given I fill in the following details on create account screen
      | Your name           | Mobile number or email | Password               | Re-enter password   |
      | <your_name>         | <mobile_email>         | <password>             | <re_enter_password> |
    Then I click on "<button>" button on create account screen
    And I should see following invalid field errors on create account screen
      | Mobile number or email                    | Password                        | Re-enter password     |
      | <mobile_email_error>                      | <password_error>                | <re_enter_pass_error> |
    Examples:
      | your_name   | mobile_email              | password  | re_enter_password | mobile_email_error                                                                    | password_error                | re_enter_pass_error     | button       |
      | abcd        | aaaa                      | 123456    | 123456            | Wrong or Invalid email address or mobile phone number. Please correct and try again.  |                               |                         | Verify email |
      | abcd        | paul.serice101@gmail.com  | 12345     | 12345             |                                                                                       | Minimum 6 characters required |                         | Verify email |
      | abcd        | paul.serice101@gmail.com  | 123456    | 12345             |                                                                                       |                               | Passwords must match    | Verify email |

  Scenario: 4 Register user - needs to bypass captcha
    Given I fill in the following details on create account screen
      | Your name           | Mobile number or email    | Password  | Re-enter password   |
      | abcd                | paul.serice101@gmail.com  | 123456    | 123456              |
    Then I click on "Verify email" button on create account screen
    And I can see solve puzzle screen with title "Solve this puzzle to protect your account"