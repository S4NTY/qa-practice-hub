@inputs
Feature: Text inputs

  As a user
  I want to practice different input controls
  So that I can enter, change, and inspect input values.

  Background:
    Given user opens inputs page

  @smoke @regression
  Scenario: User can enter text
    When user enters "Alex" in text input
    Then text input value equals "Alex"

  @regression
  Scenario: User can clear text
    When user clears text input
    Then text input is empty

  @smoke @regression
  Scenario: User can enter an email address
    When user enters "alex@example.com" in email input
    Then email input value equals "alex@example.com"

  @smoke @regression
  Scenario: User can show a password
    When user shows password
    Then password input type equals "text"

  @regression
  Scenario: User can hide a password after showing it
    When user shows and hides password
    Then password input type equals "password"

  @smoke @regression
  Scenario: User can enter a number
    When user enters 42 in number input
    Then number input value equals "42"

  @smoke @regression
  Scenario: User can enter a date
    When user enters "2026-11-08" in date input
    Then date input value equals "2026-11-08"

  @smoke @regression
  Scenario: User can enter a time
    When user enters "14:30" in time input
    Then time input value equals "14:30"

  @smoke @regression
  Scenario: User can enter a search query
    When user enters "playwright" in search input
    Then search input value equals "playwright"

  @regression
  Scenario: User can change phone country code
    When user selects phone country "uk"
    Then phone country code equals "+44"

  @smoke @regression
  Scenario: User can enter a phone number
    When user enters "9876543210" in phone input
    Then phone input value equals "9876543210"

  @smoke @regression
  Scenario: User can enter text in textarea
    When user enters "Practice makes progress" in textarea
    Then textarea value equals "Practice makes progress"

  @regression
  Scenario: Read-only input cannot be edited
    When user focuses read-only input
    Then read-only input value equals "Cannot edit this" and is read-only

  @regression
  Scenario: Disabled input remains unavailable
    When user views disabled input
    Then disabled input value equals "Disabled field" and is disabled

  @smoke @regression
  Scenario: User can see live output while typing
    When user enters "Hello, QA!" in live output input
    Then live output equals "Hello, QA!"
