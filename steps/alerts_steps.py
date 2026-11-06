import re
import pytest
from playwright.sync_api import Dialog, expect
from pytest_bdd import given, parsers, scenarios, then, when
from pages import AlertsPage

scenarios("../features/alerts.feature")


@pytest.fixture
def alerts_page(page) -> AlertsPage:
    return AlertsPage(page)


@given("user opens alerts page")
def open_alerts_page(alerts_page: AlertsPage) -> None:
    alerts_page.open()

@when("user dismisses the JavaScript alert")
def dismiss_javascript_alert(alerts_page: AlertsPage) -> None:
    alerts_page.page.once("dialog", lambda d: d.dismiss())
    alerts_page.show_alert()

@when(parsers.parse('user responds "{response}" to the confirmation dialog'))
def respond_to_confirmation_dialog(alerts_page: AlertsPage, response: str) -> None:
    if response not in {"accepts", "dismisses"}:
        raise ValueError(f"Unsupported confirmation response: {response}")

    alerts_page.page.once(
        "dialog",
        lambda d: d.accept() if response == "accepts" else d.dismiss()
    )
    alerts_page.show_confirm()

@when(parsers.parse('user enters "{name}" in the prompt without validation'))
def enter_name_in_prompt(alerts_page: AlertsPage, name: str) -> None:
    alerts_page.page.once("dialog", lambda d: d.accept(name))
    alerts_page.show_prompt()

@when("user cancels the prompt without validation")
def cancel_prompt(alerts_page: AlertsPage) -> None:
    alerts_page.page.once("dialog", lambda d: d.dismiss())
    alerts_page.show_prompt()

@when(parsers.parse('user enters "{name}" in the validated prompt'))
def enter_name_in_validated_prompt(alerts_page: AlertsPage, name: str) -> None:
    alerts_page.page.once("dialog", lambda d: d.accept(name))
    alerts_page.show_validated_prompt()

@when(parsers.parse('user submits an empty name and then "{name}" in the validated prompt'))
def retry_validated_prompt_after_empty_value(alerts_page: AlertsPage, name: str) -> None:
    prompts_seen = 0

    def handle_dialog(dialog: Dialog) -> None:
        nonlocal prompts_seen
        if dialog.type == "prompt":
            prompts_seen += 1
            dialog.accept("   " if prompts_seen == 1 else name)
        else:
            dialog.accept()

    alerts_page.page.on("dialog", handle_dialog)
    try:
        alerts_page.show_validated_prompt()
    finally:
        alerts_page.page.remove_listener("dialog", handle_dialog)

@when("user cancels the validated prompt")
def cancel_validated_prompt(alerts_page: AlertsPage) -> None:
    alerts_page.page.once("dialog", lambda d: d.dismiss())
    alerts_page.show_validated_prompt()

@when("user shows a toast notification")
def show_toast_notification(alerts_page: AlertsPage) -> None:
    alerts_page.show_toast()

@then(parsers.parse('alert output equals "{message}"'))
def alert_output_equals(alerts_page: AlertsPage, message: str) -> None:
    expect(alerts_page.get_alert_output()).to_have_text(message)

@then("toast notification is displayed")
def toast_notification_is_displayed(alerts_page: AlertsPage) -> None:
    expect(alerts_page.get_toast_message()).to_be_visible()
    expect(alerts_page.get_toast_message()).to_have_text(re.compile(r"^Toast notification at .+$"))

@then("toast notification disappears")
def toast_notification_disappears(alerts_page: AlertsPage) -> None:
    expect(alerts_page.get_toast_message()).to_be_hidden(timeout=5_000)
