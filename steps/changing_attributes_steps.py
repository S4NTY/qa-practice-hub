import re
import pytest
from playwright.sync_api import expect
from pytest_bdd import given, parsers, scenarios, then, when
from pages import ChangingAttributesPage

scenarios("../features/changing_attributes.feature")


@pytest.fixture
def changing_attributes_page(page) -> ChangingAttributesPage:
    return ChangingAttributesPage(page)


@given("user opens changing attributes page")
def open_changing_attributes_page(changing_attributes_page: ChangingAttributesPage) -> None:
    changing_attributes_page.open()

@when("user clicks the status badge when it is ready")
def click_status_badge_when_ready(changing_attributes_page: ChangingAttributesPage) -> None:
    status_badge = changing_attributes_page.get_status_badge()
    expect(status_badge).to_have_attribute("data-status", "ready", timeout=12_000)
    changing_attributes_page.click_status_badge()

@then('ready status click count equals "Ready clicks: 1"')
def ready_status_click_count_equals(changing_attributes_page: ChangingAttributesPage) -> None:
    expect(changing_attributes_page.get_status_output()).to_have_text("Ready clicks: 1")

@when('user enters "stable locator" into the input with changing ID')
def enter_text_into_input_with_changing_id(changing_attributes_page: ChangingAttributesPage) -> None:
    changing_attributes_page.get_flip_id_input().fill("stable locator")

@when("user waits for the input ID to change")
def wait_for_input_id_to_change(changing_attributes_page: ChangingAttributesPage) -> None:
    input_locator = changing_attributes_page.get_flip_id_input()
    initial_id = input_locator.get_attribute("id")
    expect(input_locator).not_to_have_attribute("id", initial_id, timeout=5_000)

@then('input with changing ID still contains "stable locator"')
def input_with_changing_id_still_contains_text(changing_attributes_page: ChangingAttributesPage) -> None:
    expect(changing_attributes_page.get_flip_id_input()).to_have_value("stable locator")
    expect(changing_attributes_page.get_flip_id_readout()).to_contain_text(re.compile(r"Current id: flip-id-[ab]"))

@when("user waits for the countdown button to become enabled")
def wait_for_countdown_button(changing_attributes_page: ChangingAttributesPage) -> None:
    expect(changing_attributes_page.get_countdown_button()).to_be_enabled(timeout=8_000)

@when("user clicks the countdown button")
def click_countdown_button(changing_attributes_page: ChangingAttributesPage) -> None:
    changing_attributes_page.click_countdown_button()

@then('countdown output equals "Submit clicked while data-ready=true"')
def countdown_output_equals(changing_attributes_page: ChangingAttributesPage) -> None:
    expect(changing_attributes_page.get_countdown_output()).to_have_text("Submit clicked while data-ready=true")

@when("user waits for the dynamic ticket href to change and opens it")
def wait_for_dynamic_ticket_href_and_open(changing_attributes_page: ChangingAttributesPage) -> None:
    link = changing_attributes_page.get_mutating_link()
    initial_href = link.get_attribute("href")
    initial_title = link.get_attribute("title")
    expect(link).not_to_have_attribute("href", initial_href, timeout=3_000)
    expect(link).not_to_have_attribute("title", initial_title)
    expect(link).to_have_attribute("title", re.compile(r"^Ticket t=\d+$"))
    changing_attributes_page.pause_timers()
    changing_attributes_page.click_mutating_link()

@then("dynamic ticket link output contains the clicked href")
def dynamic_ticket_link_output_contains_clicked_href(changing_attributes_page: ChangingAttributesPage) -> None:
    expect(changing_attributes_page.get_link_readout()).to_contain_text(
        re.compile(r"^Clicked link · href was https://qapracticehub\.com/demo-ticket\?t=\d+$")
    )

@when("user pauses changing attribute timers")
def pause_changing_attribute_timers(changing_attributes_page: ChangingAttributesPage) -> None:
    changing_attributes_page.pause_timers()

@given("changing attribute timers are paused")
def changing_attribute_timers_are_paused_given(changing_attributes_page: ChangingAttributesPage) -> None:
    changing_attributes_page.pause_timers()

@then("changing attribute timers are paused")
def changing_attribute_timers_are_paused(changing_attributes_page: ChangingAttributesPage) -> None:
    expect(changing_attributes_page.get_timer_state()).to_have_text("Paused")

@then("clock timestamp remains unchanged while timers are paused")
def clock_timestamp_remains_unchanged_while_paused(changing_attributes_page: ChangingAttributesPage) -> None:
    clock = changing_attributes_page.get_clock_button()
    timestamp = clock.get_attribute("data-timestamp")
    changing_attributes_page.page.wait_for_timeout(1_200)
    expect(clock).to_have_attribute("data-timestamp", timestamp)

@when("user resumes changing attribute timers")
def resume_changing_attribute_timers(changing_attributes_page: ChangingAttributesPage) -> None:
    changing_attributes_page.resume_timers()

@then("clock timestamp changes after timers resume")
def clock_timestamp_changes_after_resume(changing_attributes_page: ChangingAttributesPage) -> None:
    clock = changing_attributes_page.get_clock_button()
    timestamp = clock.get_attribute("data-timestamp")
    expect(clock).not_to_have_attribute("data-timestamp", timestamp, timeout=2_000)

@when(parsers.parse('user sets changing attribute speed to "{speed}"'))
def set_changing_attribute_speed(changing_attributes_page: ChangingAttributesPage, speed: str) -> None:
    changing_attributes_page.set_speed(speed)

@then(parsers.parse('changing attribute speed equals "{speed}"'))
def changing_attribute_speed_equals(changing_attributes_page: ChangingAttributesPage, speed: str) -> None:
    expect(changing_attributes_page.get_speed_select()).to_have_value(speed)

@when("user resets changing attribute widgets")
def reset_changing_attribute_widgets(changing_attributes_page: ChangingAttributesPage) -> None:
    changing_attributes_page.reset_widgets()

@then("changing attribute widgets are reset")
def changing_attribute_widgets_are_reset(changing_attributes_page: ChangingAttributesPage) -> None:
    page = changing_attributes_page
    expect(page.get_status_badge()).to_have_attribute("data-status", "idle")
    expect(page.get_status_output()).to_have_text("Ready clicks: 0")
    expect(page.get_flip_id_input()).to_have_attribute("id", "flip-id-a")
    expect(page.get_flip_id_input()).to_have_attribute("name", "flip-a")
    expect(page.get_countdown_button()).to_be_disabled()
    expect(page.get_countdown_button()).to_have_attribute("data-countdown", "5")
    expect(page.get_countdown_button()).to_have_attribute("data-ready", "false")
    expect(page.get_mutating_link()).to_have_attribute("href", "https://qapracticehub.com/demo-ticket?t=0")
