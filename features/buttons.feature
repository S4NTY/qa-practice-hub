@buttons
Feature: Buttons page

  As a user:
  I want to interact with different types of buttons
  So that I can verify their behavior, states, and side effects on the page

  Background:
    Given user opens buttons page

  @smoke @regression
  Scenario: User can clicks primary button
    When user clicks to button with text "Primary Button"
    Then button output message equals "Primary button clicked."

  @regression
  Scenario: User can clicks secondary button
    When user clicks to button with text "Secondary Button"
    Then button output message equals "Secondary button clicked."

  @regression
  Scenario: User can make left clicks
    When user clicks to button with text "Left Click Me"
    Then button output message equals "Left click detected!"

  @regression
  Scenario: User can clicks outline button
    When user clicks to button with text "Outline Button"
    Then button output message equals "Outline button clicked."

  @regression
  Scenario: User can clicks counter button
    When user clicks to button with text "Click Me (0)"
    And user clicks to button with text "Click Me (1)"
    And user clicks to button with text "Click Me (2)"
    Then button output message equals "Button clicked 3 time(s)."

  @regression
  Scenario: User can double clicks to button
    When user double clicks to button with text "Double Click Me"
    Then button output message equals "Double click detected!"

  @regression
  Scenario: User can right click to button
    When user clicks to "Right Click Me" button
    Then button output message equals "Right click detected!"

  @smoke @regression
  Scenario: User can hover to button
    When user hover to hover button
    Then button output message equals "Mouse entered the hover button."

  @regression
  Scenario: User can clicks to danger button
    When user clicks to button with text "Danger Button"
    Then button output message equals "Danger button clicked."

  @regression
  Scenario: User can navigate to next pages
    When user clicks to "Next Page" button
    Then buttons next page is opened

  @regression
  Scenario: User can go to main page from the next page
    When user clicks to "Next Page" button
    And user clicks to "Go Back" button
    Then main page is opened

  @smoke @regression
  Scenario: User can go ahead from the next page
    When user clicks to "Next Page" button
    And user clicks to "Go Ahead" button
    Then buttons ahead page is opened

  @regression
  Scenario: User can go back to next page from the ahead pages
    When user clicks to "Next Page" button
    And user clicks to "Go Ahead" button
    And user clicks to "Go Back to Previous Page" button
    Then buttons next page is opened

  @regression
  Scenario: User can go to main page from the ahead page
    When user clicks to "Next Page" button
    And user clicks to "Go Ahead" button
    And user clicks to "Go Back to Main Page" button
    Then main page is opened

  @smoke @regression
  Scenario: User can download sample file
    When user clicks to "Download Sample File" button
    Then downloaded file name is "sample.txt"
    And downloaded file content is "Hello from QA Practice Hub!\nUse this file to test download scenarios."

  @smoke @regression
  Scenario: User can open buttons selection popup
    When user clicks to button with text "Open Popup"
    Then buttons selection popup is visible

  @regression
  Scenario: User can close buttons selection popup
    When user clicks to button with text "Open Popup"
    And user close buttons selection popup
    Then buttons selection popup is hidden

  @smoke @regression
  Scenario: User can show info on click info button
    When user clicks to "Click Info" button
    Then info popup click is visible

  @regression
  Scenario: User can hide info on click info button
    When user clicks to "Click Info" button
    And user clicks to button with text "Primary Button"
    Then info popup click is hidden

  @smoke @regression
  Scenario: User can show info on hover
    When user hover to "Hover Info" button
    Then info popup hover is visible

  @regression
  Scenario: User can hide info on mouse leave
    When user hover to "Hover Info" button
    And user moves mouse away from hover info button
    Then info popup hover is hidden
