@alerts
Feature: Alerts page

  As a user
  I want to interact with the various browser dialog types — JavaScript alerts, confirmation dialogs, prompts (with and without validation), and toast notifications
  So that I can practice handling native browser dialogs, accepting and dismissing them, entering and validating input, and waiting for transient UI feedback on the page.

  Background:
    Given user opens alerts page

  @smoke @regression
  Scenario: User can dismiss a JavaScript alert
    When user dismisses the JavaScript alert
    Then alert output equals "Alert was shown and dismissed."

  @regression
  Scenario Outline: User can respond to a confirmation dialog
    When user responds "<response>" to the confirmation dialog
    Then alert output equals "Confirm result: <result>"

    Examples:
      | response | result    |
      | accepts  | Accepted  |
      | dismisses| Cancelled |

  @smoke @regression
  Scenario: User can submit a name in a prompt without validation
    When user enters "Alex" in the prompt without validation
    Then alert output equals "Prompt without validation — entered: Alex"

  @regression
  Scenario: User can cancel a prompt without validation
    When user cancels the prompt without validation
    Then alert output equals "Prompt without validation was cancelled."

  @smoke @regression
  Scenario: User can submit a name in a validated prompt
    When user enters "Alex" in the validated prompt
    Then alert output equals "Prompt with validation — entered: Alex"

  @regression
  Scenario: Validated prompt asks again after an empty response
    When user submits an empty name and then "Alex" in the validated prompt
    Then alert output equals "Prompt with validation — entered: Alex"

  @regression
  Scenario: User can cancel a validated prompt
    When user cancels the validated prompt
    Then alert output equals "Prompt with validation was cancelled."

  @smoke @regression
  Scenario: User can see a toast notification
    When user shows a toast notification
    Then toast notification is displayed
    And toast notification disappears
