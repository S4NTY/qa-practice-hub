@selection
Feature: Practice selecting options with different locator strategies

  Background:
    Given user opens selection page

  @smoke @regression
  Scenario: User can select gender
    When user select Gender "Female"
    Then gender output equals "female"

  @regression
  Scenario: Changing gender selection updates the output
    When user select Gender "Female"
    And user select Gender "Male"
    Then gender output equals "male"

  @regression
  Scenario Outline: User can select one or multiple skills
    When user select Skills "<skills>"
    Then skills output equals "<expected>"

    @smoke
    Examples: smoke
      | skills     | expected   |
      | Playwright | playwright |

    Examples: full regression
      | skills                                | expected                              |
      | Playwright, Selenium                  | selenium, playwright                  |
      | Appium, Cypress, Playwright, Selenium | selenium, playwright, cypress, appium |

  @smoke @regression
  Scenario: User can select country from dropdown
    When user select Country "France"
    Then country output equals "France"

  @regression
  Scenario: Changing country selection updates the output
    When user select Country "Canada"
    And user select Country "Russia"
    Then country output equals "Russia"

  @regression
  Scenario Outline: User can select one or multiple languages
    When user select Language "<language>"
    Then language output equals "<expected>"

    @smoke
    Examples: smoke
      | language   | expected   |
      | JavaScript | JavaScript |

    Examples: full regression
      | language                           | expected                           |
      | JavaScript, Python                 | JavaScript, Python                 |
      | Ruby, C#, JavaScript, Python, Java | JavaScript, Python, Java, C#, Ruby |

  @regression
  Scenario Outline: User can select one or multiple frameworks
    When user select Framework "<framework>"
    Then framework output equals "<expected>"

    @smoke
    Examples: smoke
      | framework   | expected   |
      | Playwright  | Playwright |

    Examples: full regression
      | framework                                            | expected                                             |
      | Selenium, Appium                                     | Selenium, Appium                                     |
      | Selenium, Playwright, Cypress, Appium, TestNG, JUnit | Selenium, Playwright, Cypress, Appium, TestNG, JUnit |

  @regression
  Scenario Outline: User can unselect frameworks
    When user select Framework "<select>"
    And user unselect Framework "<unselect>"
    Then framework output equals "<expected>"

    Examples:
      | select                                               | unselect                                             | expected      |
      | Playwright                                           | Playwright                                           | None selected |
      | Cypress, Appium, TestNG                              | Appium, TestNG                                       | Cypress       |
      | Selenium, Playwright, Cypress, Appium, TestNG, JUnit | Selenium, Playwright, Cypress, Appium, TestNG, JUnit | None selected |

  @smoke @regression
  Scenario: User can slide experience years
    When user set Experience years to 3
    Then experience output equals "3 years"

  @smoke @regression
  Scenario: User can pick color
    When user set Color to "#ff0000"
    Then color output equals "#ff0000"

  @smoke @regression
  Scenario: User can enable notification
    When user toggle notification
    Then notification output equals "On"

  @regression
  Scenario: User can disable notification
    When user toggle notification
    And user toggle notification
    Then notification output equals "Off"

  @smoke @regression
  Scenario: User can select value from autocomplete
    When user type "ind" in autocomplete
    And user select autocomplete suggestion "India"
    Then autocomplete output equals "India"
