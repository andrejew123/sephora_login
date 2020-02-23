@login

Feature: Login

    # 6
    Scenario: Ability to log in
        Given I am on log in page
        When I fill email field with correct data
        And I fill password field with correct data
        And I click on 'Zaloguj sie' button
        Then I am redirected to my account page

    # 9
    Scenario: Login failed when password field empty
        Given I am on log in page
        When I fill email field with correct data
        And I click on 'Zaloguj sie' button
        Then I see information that password field is empty