Feature: Inventory Page


  Scenario: Has 6 products on page
    Given I am on the Sign in page
    When I login successfully with "standard_user" and "secret_sauce"
    Then There are 6 products on the Inventory page

 @single
  Scenario: Redirect to login Page when unauthenticated user
    Given I am not log in user
    When I go to the Inventory Page
    Then I am redirected to Login Page
    And I receive a Sad Face message

