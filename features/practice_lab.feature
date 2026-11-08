@practice_lab
Feature: Practice Lab page

  As a user
  I want to practice multi-step forms, custom date pickers, and stale elements
  So that I can automate realistic browser interactions.

  Background:
    Given user opens Practice Lab page

  @regression @negative
  Scenario: Wizard requires personal details
    When user proceeds to the next wizard step
    Then wizard message equals "Please fill in name and email."
    And wizard step 1 is visible

  @regression @negative
  Scenario: Wizard requires address details
    Given wizard personal details are "Alex Tester" and "alex@example.com"
    And user proceeds to the next wizard step
    When user proceeds to the next wizard step
    Then wizard message equals "Please fill in city and ZIP code."
    And wizard step 2 is visible

  @smoke @regression
  Scenario: User can review all wizard details
    Given wizard personal details are "Alex Tester" and "alex@example.com"
    And user proceeds to the next wizard step
    And wizard address details are "Moscow" and "101000"
    When user proceeds to the next wizard step
    Then wizard step 3 is visible
    And wizard review contains name "Alex Tester", email "alex@example.com", city "Moscow" and ZIP "101000"

  @regression
  Scenario: Wizard preserves details when navigating back
    Given wizard personal details are "Alex Tester" and "alex@example.com"
    And user proceeds to the next wizard step
    And wizard address details are "Moscow" and "101000"
    When user returns to the previous wizard step
    Then wizard step 1 is visible
    And wizard personal fields contain "Alex Tester" and "alex@example.com"

  @regression
  Scenario: Wizard preserves address when navigating forward again
    Given wizard personal details are "Alex Tester" and "alex@example.com"
    And user proceeds to the next wizard step
    And wizard address details are "Moscow" and "101000"
    And user proceeds to the next wizard step
    And user returns to the previous wizard step
    When user proceeds to the next wizard step
    Then wizard step 3 is visible
    And wizard review contains name "Alex Tester", email "alex@example.com", city "Moscow" and ZIP "101000"

  @smoke @regression
  Scenario: User submits the completed wizard
    Given wizard personal details are "Alex Tester" and "alex@example.com"
    And user proceeds to the next wizard step
    And wizard address details are "Moscow" and "101000"
    And user proceeds to the next wizard step
    When user submits the wizard
    Then wizard message equals "Wizard submitted successfully!"
    And wizard step 1 is visible
    And wizard form fields are empty

  @smoke @regression
  Scenario: User selects a date in the custom date picker
    When user selects date "2025-01-15" in the custom date picker
    Then custom date output message equals "Selected date: 2025-01-15"
    And custom date picker is closed
    And custom date field shows "2025-01-15"

  @smoke @regression
  Scenario: Stale demo replaces its button after every click
    When user clicks the stale demo button 3 times
    Then stale demo output equals "Click count: 3"
    And stale demo button render version is 4
