Feature: Login
  As a user
  I want to log into the application
  So that I can access my inventory

  Scenario: Successful login
    Given I am on the login page
    When I login with username "standard_user" and password "secret_sauce"
    Then I should see the inventory page

  Scenario Outline: Invalid login
    Given I am on the login page
    When I login with username "<username>" and password "<password>"
    Then I should see an error containing "<message>"

    Examples:
      | username        | password     | message                                |
      | locked_out_user | secret_sauce | Sorry, this user has been locked out   |
      | standard_user   | wrong_pass   | Username and password do not match     |
