@advanced
Feature: Advanced elements page

  As a user
  I want to practice file uploads, drag and drop, Shadow DOM and progress controls
  So that I can automate advanced browser interactions.

  Background:
    Given user opens advanced page

  @smoke @regression
  Scenario: User can upload a single file
    When user uploads file "sample.txt"
    Then single file output equals "Selected: sample.txt (9 bytes)"

  @regression
  Scenario: User can clear an uploaded single file
    Given a single file has been uploaded
    When user clears the uploaded file
    Then single file output equals "No file chosen"

  @smoke @regression
  Scenario: User can upload multiple files
    When user uploads files "first.txt, second.txt"
    Then multiple files output equals "first.txt, second.txt"

  @regression
  Scenario: User can clear uploaded files
    Given multiple files have been uploaded
    When user clears the uploaded files
    Then multiple files output equals "No files chosen"

  @smoke @regression
  Scenario: User can drop a file into the drop zone
    When user drops file "dropped.txt" into the drop zone
    Then drop zone output equals "Dropped: dropped.txt"

  @regression
  Scenario: User can clear a dropped file
    Given a file named "dropped.txt" has been dropped
    When user clears the dropped file
    Then drop zone output equals "—"

  @smoke @regression
  Scenario: User can interact with a Shadow DOM button
    When user clicks the Shadow DOM button
    Then Shadow DOM output equals "Shadow DOM button clicked!"

  @regression
  Scenario: User can hide the Shadow DOM output
    Given the Shadow DOM output is visible
    When user hides the Shadow DOM output
    Then Shadow DOM output is hidden

  @smoke @regression
  Scenario: User can increase progress
    When user increases progress by 1 steps
    Then progress output equals "40%"
    And progress bar value equals 40

  @regression
  Scenario: User can decrease progress
    When user decreases progress by 1 steps
    Then progress output equals "20%"
    And progress bar value equals 20

  @regression
  Scenario: Progress cannot exceed 100 percent
    When user increases progress by 7 steps
    Then progress output equals "100%"
    And progress bar value equals 100

  @regression
  Scenario: Progress cannot go below zero
    When user decreases progress by 3 steps
    Then progress output equals "0%"
    And progress bar value equals 0