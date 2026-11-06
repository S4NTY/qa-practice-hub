import pytest
from pathlib import Path
from playwright.sync_api import expect
from pytest_bdd import given, parsers, scenarios, then, when
from pages import AdvancedPage

scenarios("../features/advanced.feature")


@pytest.fixture
def advanced_page(page) -> AdvancedPage:
    return AdvancedPage(page)


@given("user opens advanced page")
def open_advanced_page(advanced_page: AdvancedPage) -> None:
    advanced_page.open()

@given("a single file has been uploaded")
def single_file_has_been_uploaded(
    advanced_page: AdvancedPage,
    tmp_path: Path,
) -> None:
    file_path = tmp_path / "sample.txt"
    file_path.write_text("test data", encoding="utf-8")
    advanced_page.upload_file(file_path)

@when(parsers.parse('user uploads file "{filename}"'))
def upload_file(advanced_page: AdvancedPage, tmp_path: Path, filename: str) -> None:
    file_path = tmp_path / filename
    file_path.write_text("test data", encoding="utf-8")
    advanced_page.upload_file(file_path)

@when("user clears the uploaded file")
def clear_uploaded_file(advanced_page: AdvancedPage) -> None:
    advanced_page.clear_single_file()

@then(parsers.parse('single file output equals "{message}"'))
def single_file_output_equals(advanced_page: AdvancedPage, message: str) -> None:
    expect(advanced_page.get_single_file_output()).to_have_text(message)

@given("multiple files have been uploaded")
def multiple_files_have_been_uploaded(
    advanced_page: AdvancedPage,
    tmp_path: Path,
) -> None:
    file_paths = []
    for filename in ("first.txt", "second.txt"):
        file_path = tmp_path / filename
        file_path.write_text("test data", encoding="utf-8")
        file_paths.append(file_path)
    advanced_page.upload_multiple_files(file_paths)

@when(parsers.parse('user uploads files "{filenames}"'))
def upload_multiple_files(
    advanced_page: AdvancedPage,
    tmp_path: Path,
    filenames: str,
) -> None:
    file_paths = []
    for filename in filenames.split(","):
        filename = filename.strip()
        file_path = tmp_path / filename
        file_path.write_text("test data", encoding="utf-8")
        file_paths.append(file_path)
    advanced_page.upload_multiple_files(file_paths)

@when("user clears the uploaded files")
def clear_uploaded_files(advanced_page: AdvancedPage) -> None:
    advanced_page.clear_multiple_files()

@then(parsers.parse('multiple files output equals "{message}"'))
def multiple_files_output_equals(advanced_page: AdvancedPage, message: str) -> None:
    expect(advanced_page.get_multiple_files_output()).to_have_text(message)

@when(parsers.parse('user drops file "{filename}" into the drop zone'))
def drop_file(advanced_page: AdvancedPage, filename: str) -> None:
    advanced_page.drop_file(filename, "test data")

@given(parsers.parse('a file named "{filename}" has been dropped'))
def dropped_file_has_been_dropped(advanced_page: AdvancedPage, filename: str) -> None:
    advanced_page.drop_file(filename, "test data")

@when("user clears the dropped file")
def clear_dropped_file(advanced_page: AdvancedPage) -> None:
    advanced_page.clear_dropped_files()

@then(parsers.parse('drop zone output equals "{message}"'))
def drop_zone_output_equals(advanced_page: AdvancedPage, message: str) -> None:
    expect(advanced_page.get_drop_output()).to_have_text(message)

@when("user clicks the Shadow DOM button")
def click_shadow_button(advanced_page: AdvancedPage) -> None:
    advanced_page.click_shadow_button()

@given("the Shadow DOM output is visible")
def shadow_dom_output_is_visible(advanced_page: AdvancedPage) -> None:
    advanced_page.click_shadow_button()

@when("user hides the Shadow DOM output")
def hide_shadow_output(advanced_page: AdvancedPage) -> None:
    advanced_page.hide_shadow_output()

@then(parsers.parse('Shadow DOM output equals "{message}"'))
def shadow_dom_output_equals(advanced_page: AdvancedPage, message: str) -> None:
    expect(advanced_page.get_shadow_output()).to_have_text(message)

@then("Shadow DOM output is hidden")
def shadow_dom_output_is_hidden(advanced_page: AdvancedPage) -> None:
    expect(advanced_page.get_shadow_output()).to_be_hidden()

@when(parsers.parse("user increases progress by {times:d} steps"))
def increase_progress(advanced_page: AdvancedPage, times: int) -> None:
    advanced_page.increase_progress(times)

@when(parsers.parse("user decreases progress by {times:d} steps"))
def decrease_progress(advanced_page: AdvancedPage, times: int) -> None:
    advanced_page.decrease_progress(times)

@then(parsers.parse('progress output equals "{message}"'))
def progress_output_equals(advanced_page: AdvancedPage, message: str) -> None:
    expect(advanced_page.get_progress_output()).to_have_text(message)

@then(parsers.parse("progress bar value equals {value:d}"))
def progress_bar_value_equals(advanced_page: AdvancedPage, value: int) -> None:
    expect(advanced_page.get_progress_bar()).to_have_js_property("value", value)