import pytest
from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers
from pages.tables_page import TablesPage, TableRow
from steps.common_steps import *

scenarios("../features/tables.feature")


@pytest.fixture
def tables_page(page):
    return TablesPage(page)

@pytest.fixture
def users() -> list[TableRow]:
    return []


@given("user opens tables page")
def open_tables_page(tables_page: TablesPage) -> None:
    tables_page.open()

@when(parsers.parse('user filters by name "{name}"'))
def filter_by_name(tables_page: TablesPage, name: str) -> None:
    tables_page.filter_by_name(name)

@then(parsers.parse('table selection output equals "{message}"'))
def table_selection_output_equals(tables_page: TablesPage, message: str) -> None:
    expect(tables_page.get_table_selection_output()).to_have_text(message)

@when("user selects all rows in the table")
def select_all_rows_in_the_table(tables_page: TablesPage) -> None:
    tables_page.select_all_rows_input_click()

@when("user goes to next page")
def go_to_next_page(tables_page: TablesPage) -> None:
    tables_page.page_next_button_click()

@when("user goes to previous page")
def go_to_previous_page(tables_page: TablesPage) -> None:
    tables_page.page_prev_button_click()

@then(parsers.parse('page info equals "{message}"'))
def table_selection_output_equals(tables_page: TablesPage, message: str) -> None:
    expect(tables_page.get_page_info()).to_have_text(message)

@then(parsers.parse('form message error equals "{message}"'))
def form_message_error_equals(tables_page: TablesPage, message: str) -> None:
    expect(tables_page.get_form_message_error()).to_have_text(message)

@when(parsers.parse('user delete row by user id {id}'))
def delete_row_by_user_id(tables_page: TablesPage, id: int) -> None:
    tables_page.delete_row_by_id(id)

@then(parsers.parse('table contains only users with name containing "{name}"'))
def table_contains_only_users_with_name(tables_page: TablesPage, name: str) -> None:
    rows: TableRow = tables_page.get_rows()
    for row in rows:
        assert name in row.name

@when(parsers.parse('user selects rows with ids "{ids}"'))
def select_rows_with_ids(tables_page: TablesPage, ids: str) -> None:
    for id in ids.split(','):
        tables_page.select_checkbox_by_id(id.strip())

@then("added users are shown in the table")
def added_users_are_shown_in_the_table(tables_page: TablesPage, users: list[TableRow]):
    actual = {row.id: row for row in tables_page.get_rows()}
    for expected in users:
        assert expected.id in actual
        assert actual[expected.id] == expected

@then(parsers.parse('user ids start from {id:d}'))
def user_ids_start_from(tables_page: TablesPage, id: int):
    rows = tables_page.get_rows()
    assert rows[0].id == id

@when(parsers.parse('user fills user {index} form with:'))
def fill_user_form(tables_page: TablesPage, datatable, index, users):
    headers, *rows = datatable
    for row in rows:
        data = dict(zip(headers, row))
        data["index"] = index
        tables_page.fill_user(**data)
        users.append(
            TableRow(
                id=int(data["id"]),
                name=data["name"],
                email=data["email"],
                role=data["role"],
                age=int(data["age"]),
            )
        )
