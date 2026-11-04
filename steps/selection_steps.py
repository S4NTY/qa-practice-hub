import pytest
from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers
from pages import SelectionPage
from steps.common_steps import *

scenarios("../features/selection.feature")


@pytest.fixture
def selection_page(page) -> SelectionPage:
    return SelectionPage(page)


@given("user opens selection page")
def open_selection_page(selection_page: SelectionPage) -> None:
    selection_page.open()

@when(parsers.parse('user select Gender "{gender}"'))
def select_gender(selection_page: SelectionPage, gender: str) -> None:
    selection_page.select_gender(gender)

@then(parsers.parse('gender output equals "{message}"'))
def gender_output_equals(selection_page: SelectionPage, message: str) -> None:
    expect(selection_page.get_gender_output()).to_have_text(message)

@when(parsers.parse('user select Skills "{skills}"'))
def select_skills(selection_page: SelectionPage, skills: str) -> None:
    skill_list = [s.strip().lower() for s in skills.split(",")]
    for skill in skill_list:
        selection_page.select_skill(skill)

@then(parsers.parse('skills output equals "{message}"'))
def skills_output_equals(selection_page: SelectionPage, message: str) -> None:
    expect(selection_page.get_skills_output()).to_have_text(message)

@when(parsers.parse('user select Country "{country}"'))
def select_country(selection_page: SelectionPage, country: str) -> None:
    selection_page.select_country_by_text(country)

@then(parsers.parse('country output equals "{message}"'))
def country_output_equals(selection_page: SelectionPage, message: str) -> None:
    expect(selection_page.get_country_output()).to_have_text(message)

@when(parsers.parse('user select Language "{languages}"'))
def select_language(selection_page: SelectionPage, languages: str) -> None:
    language_list = [s.strip() for s in languages.split(",")]
    selection_page.select_languages(*language_list)

@then(parsers.parse('language output equals "{message}"'))
def language_output_equals(selection_page: SelectionPage, message: str) -> None:
    expect(selection_page.get_languages_output()).to_have_text(message)

@when(parsers.parse('user select Framework "{framework}"'))
def select_framework(selection_page: SelectionPage, framework: str) -> None:
    framework_list = [s.strip().lower() for s in framework.split(",")]
    selection_page.select_frameworks(*framework_list)

@when(parsers.parse('user unselect Framework "{framework}"'))
def unselect_framework(selection_page: SelectionPage, framework: str) -> None:
    framework_list = [s.strip().lower() for s in framework.split(",")]
    selection_page.unselect_frameworks(*framework_list)

@then(parsers.parse('framework output equals "{message}"'))
def framework_output_equals(selection_page: SelectionPage, message: str) -> None:
    expect(selection_page.get_frameworks_output()).to_have_text(message)

@when(parsers.parse('user set Experience years to {years}'))
def set_experience_years(selection_page: SelectionPage, years: int) -> None:
    selection_page.set_experience(years)

@then(parsers.parse('experience output equals "{message}"'))
def experience_output_equals(selection_page: SelectionPage, message: str) -> None:
    expect(selection_page.get_experience_output()).to_have_text(message)

@when(parsers.parse('user set Color to "{color}"'))
def set_color(selection_page: SelectionPage, color: str) -> None:
    selection_page.set_color(color)

@then(parsers.parse('color output equals "{message}"'))
def color_output_equals(selection_page: SelectionPage, message: str) -> None:
    expect(selection_page.get_color_output()).to_have_text(message)

@when("user toggle notification")
def set_color(selection_page: SelectionPage) -> None:
    selection_page.toggle_notifications()

@then(parsers.parse('notification output equals "{message}"'))
def notification_output_equals(selection_page: SelectionPage, message: str) -> None:
    expect(selection_page.get_toggle_output()).to_have_text(message)

@when(parsers.parse('user type "{autocomplete}" in autocomplete'))
def type_autocomplete(selection_page: SelectionPage, autocomplete: str) -> None:
    selection_page.type_autocomplete(autocomplete)

@when(parsers.parse('user select autocomplete suggestion "{suggestion}"'))
def select_autocomplete_suggestion(selection_page: SelectionPage, suggestion: str) -> None:
    selection_page.select_autocomplete_suggestion(suggestion)

@then(parsers.parse('autocomplete output equals "{message}"'))
def autocomplete_output_equals(selection_page: SelectionPage, message: str) -> None:
    expect(selection_page.get_autocomplete_output()).to_have_text(message)
