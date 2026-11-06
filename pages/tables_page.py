from pages.base_page import BasePage
from playwright.sync_api import Page, Locator
from dataclasses import dataclass, fields


@dataclass
class TableRow:
    id: int
    name: str
    email: str
    role: str
    age: int


class TablesPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.users_table_body = page.get_by_test_id("users-table-body")
        self.table_search_input = page.get_by_test_id("table-search")
        self.select_all_rows_input = page.get_by_test_id("select-all-rows")
        self.table_selection_output_label = page.get_by_test_id("table-selection-output")
        self.page_prev_button = page.get_by_test_id("page-prev")
        self.page_next_button = page.get_by_test_id("page-next")
        self.page_info_label = page.get_by_test_id("page-info")
        self.form_message_error_label = page.get_by_test_id("add-role-message")


    def open(self) -> None:
        super().open("#tables")

    def get_table_selection_output(self) -> Locator:
        return self.table_selection_output_label

    def get_page_info(self) -> Locator:
        return self.page_info_label

    def get_form_message_error(self) -> Locator:
        return self.form_message_error_label

    def get_rows(self) -> list[TableRow]:
        rows: list[TableRow] = []
        for row in self.users_table_body.locator("tr").all():
            id_, name, email, role, age = row.locator("td").all_inner_texts()[1:-1]
            rows.append(TableRow(int(id_), name, email, role, int(age)))
        return rows

    def fill_user(
            self,
            id: str | int,
            name: str,
            email: str,
            role: str,
            age: str | int,
            index: int = 1,
    ) -> None:
        self.page.get_by_test_id(f"role-id-{index}").fill(str(id))
        self.page.get_by_test_id(f"role-name-{index}").fill(name)
        self.page.get_by_test_id(f"role-email-{index}").fill(email)
        self.page.get_by_test_id(f"role-role-{index}").select_option(role)
        self.page.get_by_test_id(f"role-age-{index}").fill(str(age))

    def filter_by_name(self, name: str) -> None:
        self.table_search_input.fill(name)

    def select_checkbox_by_id(self, id: str) -> None:
        self.page.locator(f'input[data-user-id="{id}"]').check()

    def delete_row_by_id(self, id: str) -> None:
        self.page.locator(f'button[data-user-id="{id}"]').click()

    def select_all_rows_input_click(self) -> None:
        self.select_all_rows_input.click()

    def page_prev_button_click(self) -> None:
        self.page_prev_button.click()

    def page_next_button_click(self) -> None:
        self.page_next_button.click()
