import pytest
from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers
from pages import OTPLoginPage, OTPFetchPage, OTPResendPage
from steps.common_steps import *

scenarios("../features/otp_login.feature")


@pytest.fixture
def otp_login_page(page) -> OTPLoginPage:
    return OTPLoginPage(page)


@given("user opens otp login page")
def open_otp_login_page(otp_login_page: OTPLoginPage) -> None:
    otp_login_page.open()

@given("user closes fetch page")
def close_fetch_page(otp_fetch_page: OTPFetchPage) -> None:
    otp_fetch_page.close()

@given("user closes resend page")
def close_resend_page(otp_resend_page: OTPResendPage) -> None:
    otp_resend_page.close()

@when(parsers.re(r'user enters "(?P<username>.*)" to the username field'))
@given(parsers.re(r'user enters "(?P<username>.*)" to the username field'))
def enters_to_username_field(otp_login_page: OTPLoginPage, username) -> None:
    otp_login_page.otp_username_input_set_text(username)

@when("user enters copied one time password into the otp inputs")
def enters_copied_one_time_password_into_the_otp_inputs(otp_login_page: OTPLoginPage, otp_code) -> None:
    otp_login_page.set_one_time_password(otp_code)

@when(parsers.parse('user enters "{code}" into the otp inputs'))
def enters_copied_code_into_the_otp_inputs(otp_login_page: OTPLoginPage, code) -> None:
    otp_login_page.set_one_time_password(code)

@then(parsers.parse('otp login message equals "{message}"'))
def otp_login_message_equals(otp_login_page: OTPLoginPage, message: str) -> None:
    expect(otp_login_page.get_otp_login_message_label()).to_have_text(message)

@given("user copies the OTP from the fetch page", target_fixture="otp_code")
def copy_otp_from_fetch_page(otp_fetch_page: OTPFetchPage) -> str:
    return otp_fetch_page.otp_display_label_get_text()

@given("user copies the OTP from the resend page", target_fixture="otp_code")
def copy_otp_from_resend_page(otp_resend_page: OTPResendPage) -> str:
    return otp_resend_page.otp_display_label_get_text()

@when('user clicks to "Fetch OTP" button', target_fixture="otp_fetch_page")
def fetch_otp_button_click(otp_login_page: OTPLoginPage) -> OTPFetchPage:
    return otp_login_page.otp_fetch_button_click()

@when('user clicks to "Resend OTP" button', target_fixture="otp_resend_page")
def resend_otp_button_click(otp_login_page: OTPLoginPage) -> OTPResendPage:
    return otp_login_page.otp_resend_button_click()

@then("there is a timer on the fetch page")
def there_is_a_timer_on_the_fetch_page(otp_fetch_page: OTPFetchPage) -> None:
    expect(otp_fetch_page.get_otp_close_countdown_label()).to_be_visible()

@then(parsers.re(r"fetch button is (?P<state>enabled|disabled)"))
def fetch_button_state(otp_login_page: OTPLoginPage, state: str) -> None:
    expect(otp_login_page.get_otp_fetch_button()).to_be_enabled(enabled=(state == "enabled"))

@then(parsers.re(r"resend button is (?P<state>visible|hidden)"))
def resend_button_state(otp_login_page: OTPLoginPage, state: str) -> None:
    expect(otp_login_page.get_otp_resend_button()).to_be_visible(visible=(state == "visible"))

@when(parsers.parse("had passed {seconds} seconds"))
def fast_forward_time(otp_login_page: OTPLoginPage, seconds: int) -> None:
    otp_login_page.page.clock.install()
    otp_login_page.page.clock.fast_forward(int(seconds) * 1000)

@then("timer on the fetch page is counting down")
def timer_is_counting_down(otp_fetch_page: OTPFetchPage) -> None:
    initial = otp_fetch_page.get_otp_close_countdown_value()
    timer = otp_fetch_page.get_otp_close_countdown_label()
    expect(timer).not_to_have_text(initial, timeout=3_000)

@then("otp fetch page is opened")
def otp_fetch_page_is_opened(otp_fetch_page: OTPFetchPage) -> None:
    otp_fetch_page.should_have_url("https://qapracticehub.com/otp-fetch.html")
    expect(otp_fetch_page.get_otp_fetch_title_label()).to_have_text("Fresh OTP")

@then("otp resend page is opened")
def otp_resend_page_is_opened(otp_resend_page: OTPResendPage) -> None:
    otp_resend_page.should_have_url("https://qapracticehub.com/otp-resend.html")
    expect(otp_resend_page.get_otp_resend_title_label()).to_have_text("Resend OTP")

@when(parsers.parse('user fetched OTP for username "{username}"'), target_fixture="otp_code")
@given(parsers.parse('user fetched OTP for username "{username}"'), target_fixture="otp_code")
def fetch_otp(otp_login_page: OTPLoginPage, username: str) -> str:
    enters_to_username_field(otp_login_page, username)
    fetch_page = fetch_otp_button_click(otp_login_page)
    otp_fetch_page_is_opened(fetch_page)
    code = copy_otp_from_fetch_page(fetch_page)
    close_fetch_page(fetch_page)
    return code

@given("user resent OTP", target_fixture="otp_code")
def resend_otp(otp_login_page: OTPLoginPage) -> str:
    resend_page = resend_otp_button_click(otp_login_page)
    otp_resend_page_is_opened(resend_page)
    code = copy_otp_from_resend_page(resend_page)
    close_resend_page(resend_page)
    return code
