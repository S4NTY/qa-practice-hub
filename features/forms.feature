@forms
Feature: Forms page

  As a user:
  I want to be able to log in, recover my password, and register on the Forms page so that
  I can quickly access my account or create a new one.

  Background:
    Given user opens forms page

  @smoke @regression
  Scenario: Successful login
    When user enters login "tester" and password "password123" to login form
    And user clicks to button with text "Login"
    Then login message equals "Login successful! Welcome, tester."

  @regression @negative
  Scenario: Login with non-existent user
    When user enters login "tester" and password "password" to login form
    And user clicks to button with text "Login"
    Then login message equals "Invalid credentials. Try username: tester, password: password123"

  @regression
  Scenario: Forgot password for existent user
    When user clicks to button with text "Forgot password?"
    And user enters "tester" to username field on forgot password form
    And user clicks to button with text "Submit"
    Then forgot password result equals "Password: password123"

  @regression @negative
  Scenario: Forgot password for non-existent user
    When user clicks to button with text "Forgot password?"
    And user enters "admin" to username field on forgot password form
    And user clicks to button with text "Submit"
    Then forgot password message equals "Username not found."

  @smoke @regression
  Scenario: Successful registration
    When user enters "John" to the first name field
    And user enters "Smith" to the last name field
    And user enters "johnsmith@gmail.com" to the email field
    And user selects country "Russia"
    And user clicks to button with text "Register"
    Then register message equals "Registration successful for John Smith!"

  @regression
  Scenario: Clear registration form
    When user enters "John" to the first name field
    And user enters "Smith" to the last name field
    And user enters "johnsmith@gmail.com" to the email field
    And user selects country "Russia"
    And user clicks to button with text "Clear"
    Then registration form is empty

  @regression @negative
  Scenario Outline: Registration with a missing required field is rejected
    When user enters "<first>" to the first name field
    And user enters "<last>" to the last name field
    And user enters "<email>" to the email field
    And user selects country "Russia"
    And user clicks to button with text "Register"
    Then register message equals "Please fill in all required fields."

    Examples:
      | first | last  | email               |
      |       | Smith | johnsmith@gmail.com |
      | John  |       | johnsmith@gmail.com |
      | John  | Smith |                     |
      |       |       | johnsmith@gmail.com |
