from pathlib import Path
from pages.base_page import BasePage
from playwright.sync_api import Locator, Page


class AdvancedPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._single_file_input = page.get_by_test_id("file-upload")
        self._single_file_output = page.get_by_test_id("file-upload-output")
        self._single_file_clear_button = page.get_by_test_id("file-upload-clear")
        self._multiple_files_input = page.get_by_test_id("file-upload-multiple")
        self._multiple_files_output = page.get_by_test_id("file-multiple-output")
        self._multiple_files_clear_button = page.get_by_test_id("file-multiple-clear")
        self._drop_zone = page.get_by_test_id("drop-zone")
        self._drop_output = page.get_by_test_id("drop-output")
        self._drop_clear_button = page.get_by_test_id("drop-zone-clear")
        self._shadow_button = page.get_by_test_id("shadow-button")
        self._shadow_output = page.get_by_test_id("shadow-output")
        self._shadow_hide_button = page.get_by_test_id("shadow-hide-button")
        self._progress_bar = page.get_by_test_id("progress-bar")
        self._progress_output = page.get_by_test_id("progress-output")
        self._progress_increase_button = page.get_by_test_id("btn-progress-inc")
        self._progress_decrease_button = page.get_by_test_id("btn-progress-dec")


    def open(self) -> None:
        super().open("#advanced")

    def get_single_file_output(self) -> Locator:
        return self._single_file_output

    def get_multiple_files_output(self) -> Locator:
        return self._multiple_files_output

    def get_drop_output(self) -> Locator:
        return self._drop_output

    def get_shadow_output(self) -> Locator:
        return self._shadow_output

    def get_progress_output(self) -> Locator:
        return self._progress_output

    def get_progress_bar(self) -> Locator:
        return self._progress_bar

    def upload_file(self, file_path: str | Path) -> None:
        self._single_file_input.set_input_files(str(file_path))

    def clear_single_file(self) -> None:
        self._single_file_clear_button.click()

    def upload_multiple_files(self, file_paths: list[str | Path]) -> None:
        self._multiple_files_input.set_input_files([str(path) for path in file_paths])

    def clear_multiple_files(self) -> None:
        self._multiple_files_clear_button.click()

    def drop_file(self, filename: str, content: str) -> None:
        self.page.evaluate(
            """({filename, content}) => {
                const zone = document.querySelector('[data-testid="drop-zone"]');
                const transfer = new DataTransfer();
                transfer.items.add(new File([content], filename, {type: "text/plain"}));
                zone.dispatchEvent(new DragEvent("dragover", {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: transfer
                }));
                zone.dispatchEvent(new DragEvent("drop", {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: transfer
                }));
            }""",
            {"filename": filename, "content": content},
        )

    def clear_dropped_files(self) -> None:
        self._drop_clear_button.click()

    def click_shadow_button(self) -> None:
        self._shadow_button.click()

    def hide_shadow_output(self) -> None:
        self._shadow_hide_button.click()

    def increase_progress(self, times: int = 1) -> None:
        for _ in range(times):
            self._progress_increase_button.click()

    def decrease_progress(self, times: int = 1) -> None:
        for _ in range(times):
            self._progress_decrease_button.click()
