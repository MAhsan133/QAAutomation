Feature: User Signin Screen

  Scenario: 1 Verify signin screen detail
    Given I open amazon home page
    Then I click on "Sign-In" link on the home page
    And I should see signin screen is shown with title 'Sign-In'
    Then I should see following fields shown on signin screen
      | Email or mobile phone number |
      |                              |
    And I should see "Continue" button is shown under email field of signin screen
    When I click on "Continue" button on signin screen
    Then I should see following errors under fields on signin screen
      | Email or mobile phone number                |
      | Enter your email or mobile phone number     |

  Scenario Outline: 2 Validate invalid email /mobile field on signin screen
    Given I fill in the following details on signin screen
      | Email or mobile        |
      | <email_mobile>         |
    Then I click on "Continue" button on signin screen
    And I should see following errors on signin screen
      | Mobile number or email                    |
      | <mobile_email_error>                      |
    Examples:
      | email_mobile | mobile_email_error                                 |
      | aaaaa        | We cannot find an account with that email address  |
      | 00000        | We cannot find an account with that mobile number  |

  Scenario: 3 Validate password field on sign in screen
    Given I fill in the following details on signin screen
      | Email or mobile           |
      | ahsanattar133@gmail.com   |
    Then I click on "Continue" button on signin screen
    Then I should see following fields shown on signin screen
      | Password    |
      |             |
    Then I click on "Sign-In" button on signin screen
    And I should see following errors under fields on signin screen
      | Password                    |
      | Enter your password         |
    When I fill in the following details on signin screen
      | Password      |
      | 12345         |
    Then I click on "Sign-In" button on signin screen
    And I should see following errors on signin screen
      | Password                    |
      | Your password is incorrect  |

  Scenario: 4 Verify create account screen from signin screen
    Given I open amazon home page
    Then I click on "Sign-In" link on the home page
    And I should see signin screen is shown with title 'Sign-In'
    And I should see "Create your Amazon account" button is shown at the bottom of signin screen
    And I click on "Create your Amazon account" button on signin screen
    And I should see registration screen is shown with title 'Create account'