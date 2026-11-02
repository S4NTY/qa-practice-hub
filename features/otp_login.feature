@otp_login
Feature: Login with a one-time password

  As a user:
  I want to log in with a one-time password (OTP)
  so that I can access my account securely without having to remember or manage a permanent password.

  Business rules:
  - A username is required; without it, login is rejected.
  - Fetch OTP is enabled only when a username is entered; Resend is hidden until an OTP has been fetched.
  - After Fetch, Fetch OTP is disabled and Resend OTP becomes available.
  - Login works only with a valid OTP requested for the entered username (via Fetch or Resend).
  - An OTP expires after 30 seconds; an expired OTP is rejected, and a new one can be requested via Resend.
  - Login without a requested OTP is rejected.

  Background:
    Given user opens otp login page

  @regression
  Scenario Outline: Fetch and Resend availability depends on the username
    When user enters "<username>" to the username field
    Then fetch button is <fetch_state>
    And resend button is <resend_state>

    Examples:
      | username | fetch_state | resend_state |
      |          | disabled    | hidden       |
      | Michael  | enabled     | hidden       |

  @regression @negative
  Scenario: Login without a username is rejected
    When user clicks to button with text "Submit"
    Then otp login message equals "Please enter your username."

  @smoke @regression
  Scenario: User logs in with the fetched OTP
    Given user fetched OTP for username "John"
    When user enters copied one time password into the otp inputs
    And user clicks to button with text "Submit"
    Then otp login message equals "Login successful! Welcome, John."

  @regression
  Scenario: Fetch page shows the OTP and a decreasing countdown
    Given user enters "Steve" to the username field
    When user clicks to "Fetch OTP" button
    Then otp fetch page is opened
    And there is a timer on the fetch page
    And timer on the fetch page is counting down

  @regression @negative
  Scenario: Login with an OTP that was never requested is rejected
    When user enters "Alex" to the username field
    And user enters "123456" into the otp inputs
    And user clicks to button with text "Submit"
    Then otp login message equals "No OTP found. Enter your username and click Fetch OTP first."

  @regression
  Scenario: Resend becomes available after fetch closed
    When user fetched OTP for username "Kate"
    Then fetch button is disabled
    And resend button is visible

  @smoke @regression
  Scenario: User logs in with the resent OTP
    Given user fetched OTP for username "Nick"
    And user resent OTP
    When user enters copied one time password into the otp inputs
    And user clicks to button with text "Submit"
    Then otp login message equals "Login successful! Welcome, Nick."

  @regression @negative
  Scenario: Login with an expired fetched OTP is rejected
    Given user fetched OTP for username "Mark"
    When had passed 30 seconds
    And user enters copied one time password into the otp inputs
    And user clicks to button with text "Submit"
    Then otp login message equals "OTP has expired. Click Resend OTP to get a new code."

  @regression @negative
  Scenario: Login with an expired resent OTP is rejected
    Given user fetched OTP for username "Mary"
    And user resent OTP
    When had passed 30 seconds
    And user enters copied one time password into the otp inputs
    And user clicks to button with text "Submit"
    Then otp login message equals "OTP has expired. Click Resend OTP to get a new code."
