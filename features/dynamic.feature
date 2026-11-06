@dynamic
Feature: Dynamic content page

  As a user
  I want to interact with dynamic content on the page (manage a list of items, load data with delays, switch between tabs,
  work with a form inside an iframe, and toggle hidden text)
  So that I can practice and verify asynchronous behaviour, dynamic updates, tab navigation and iframe interactions.

  Background:
    Given user opens dynamic page

  @smoke @regression
  Scenario: User can add a new item to the dynamic list
    When user adds a new item to the dynamic list
    Then dynamic list contains "Item 1, Item 2, Item 3"

  @regression
  Scenario: User can remove the last item from the dynamic list
    When user removes the last item from the dynamic list
    Then dynamic list contains "Item 1"

  @regression
  Scenario: User can add and then remove an item from the dynamic list
    When user adds a new item to the dynamic list
    And user removes the last item from the dynamic list
    Then dynamic list contains "Item 1, Item 2"

  @smoke @regression
  Scenario: User can load data after a delay
    When user clicks the Load Data button
    Then data loading spinner is visible
    And loaded data is displayed

  @smoke @regression
  Scenario: User can load data with a custom delay
    When user sets custom delay to 500 ms
    And user loads data with custom delay
    Then custom delay result equals "Loaded after 500ms delay."

  @regression
  Scenario Outline: User can switch between practice tabs
    When user selects the "<tab>" tab
    Then the "<tab>" tab displays "<content>"

    @smoke
    Examples: smoke
      | tab      | content                                 |
      | Profile  | Profile settings and user info go here. |

    Examples: full regression
      | tab      | content                                 |
      | Home     | Welcome to the Home tab content.        |
      | Settings | Application settings and preferences.   |

  @smoke @regression
  Scenario: User can submit the iframe form
    When user fills the iframe form with name "Alex Tester", email "alex@example.com", role "Tester", and message "Practice iframe form"
    And user submits the iframe form
    Then iframe form message equals "Successfully updated user data."
    And iframe form fields are empty

  @regression @negative
  Scenario: User cannot submit the empty iframe form
    When user submits the iframe form
    Then iframe form message equals "Please fill in name, email, and role."

  @regression
  Scenario: User can clear the iframe form
    When user fills the iframe form with name "Alex Tester", email "alex@example.com", role "Tester", and message "Practice iframe form"
    And user clicks Clear in the iframe form
    Then iframe form fields are empty
    And iframe form message is hidden

  @smoke @regression
  Scenario: User can show and hide text in the iframe
    When user clicks the iframe text toggle
    Then iframe hidden text is visible
    When user clicks the iframe text toggle
    Then iframe hidden text is hidden
