@tables
Feature: Tables page

  As a user:
  I want to manage and interact with a data table (filter, select rows, paginate, sort, delete and add users)
  So that I can efficiently view, search, organize and update the list of users.

  Background:
    Given user opens tables page

  @smoke @regression
  Scenario: User can filter table data by name
    When user filters by name "Grace"
    Then table contains only users with name containing "Grace"

  @regression
  Scenario: User can select specific rows
    When user selects rows with ids "2, 3, 4"
    Then table selection output equals "3 row(s) selected"

  @regression
  Scenario: User can select all rows
    When user selects all rows in the table
    Then table selection output equals "4 row(s) selected"

  @regression
  Scenario: User can navigate to next page
    When user goes to next page
    Then page info equals "Page 2 of 2"
    And user ids start from 5

  @regression
  Scenario: User can navigate to previous page
    When user goes to next page
    And user goes to previous page
    Then page info equals "Page 1 of 2"
    And user ids start from 1

  @regression
  Scenario: User sort users by name
    When user clicks to button with text "Sort by Name"
    Then user ids start from 1

  @regression
  Scenario: User sort users by age
    When user clicks to button with text "Sort by Age"
    Then user ids start from 7

  @regression
  Scenario: User can delete row by user id
    When user delete row by user id 1
    Then user ids start from 2

  @smoke @regression
  Scenario: User can add a single new user
    When user clicks to button with text "Add New User"
    And user fills user 1 form with:
      | id  | name          | email                  | role      | age |
      | 9   | John Smith    | john.smith@example.com | Developer | 28  |
    And user clicks to button with text "Save Users"
    Then added users are shown in the table

  @regression
  Scenario: User can add multiple users
    When user clicks to button with text "Add New User"
    And user fills user 1 form with:
      | id | name          | email                    | role      | age |
      | 9  | Olivia Brown  | olivia.brown@example.com | Developer | 34  |
    And user clicks to button with text "+ Add Another"
    And user fills user 2 form with:
      | id | name          | email                     | role   | age |
      | 10 | Daniel Wilson | daniel.wilson@example.com | Tester | 29  |
    And user clicks to button with text "Save Users"
    Then added users are shown in the table

  @regression @negative
  Scenario: User can`t add user with existing id
    When user clicks to button with text "Add New User"
    And user fills user 1 form with:
      | id | name          | email                 | role  | age |
      | 1  | James Lee     | james.lee@example.com | Admin | 30  |
    And user clicks to button with text "Save Users"
    Then form message error equals "ID 1 already exists. Please use a unique ID."

  @regression @negative
  Scenario: User cannot add a user with empty fields
    When user clicks to button with text "Add New User"
    And user fills user 1 form with:
      | id | name | email | role | age |
      | 9  |      |       |      | 28  |
    And user clicks to button with text "Save Users"
    Then form message error equals "Please fill in all fields (ID, Name, Email, Role, Age)."
