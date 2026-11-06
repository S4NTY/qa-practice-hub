@changing_attributes
Feature: Changing attributes page

  As a user
  I want to interact with elements whose attributes change over time (status badge, input ID, countdown button, dynamic links, timers and speed controls)
  So that I can practice working with unstable locators, waiting for state changes, and controlling dynamic behaviour on the page.

  Background:
    Given user opens changing attributes page

  @smoke @regression
  Scenario: User can click the rotating status badge when it is ready
    When user clicks the status badge when it is ready
    Then ready status click count equals "Ready clicks: 1"

  @regression
  Scenario: User can locate the input while its ID changes
    When user enters "stable locator" into the input with changing ID
    And user waits for the input ID to change
    Then input with changing ID still contains "stable locator"

  @smoke @regression
  Scenario: User can click the countdown button when it is enabled
    When user waits for the countdown button to become enabled
    And user clicks the countdown button
    Then countdown output equals "Submit clicked while data-ready=true"

  @regression
  Scenario: User can open the dynamic ticket link after its href changes
    When user waits for the dynamic ticket href to change and opens it
    Then dynamic ticket link output contains the clicked href

  @regression
  Scenario: User can pause changing attributes
    When user pauses changing attribute timers
    Then changing attribute timers are paused
    And clock timestamp remains unchanged while timers are paused

  @regression
  Scenario: User can resume changing attributes
    Given changing attribute timers are paused
    When user resumes changing attribute timers
    Then clock timestamp changes after timers resume

  @regression
  Scenario: User can change the attribute update speed
    When user sets changing attribute speed to "2"
    Then changing attribute speed equals "2"

  @regression
  Scenario: User can reset changing attribute widgets
    When user resets changing attribute widgets
    Then changing attribute widgets are reset
