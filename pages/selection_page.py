from pages.base_page import BasePage
from playwright.sync_api import Page, Locator
from typing import Literal

Gender = Literal["male", "female", "other"]
Skill = Literal["selenium", "playwright", "cypress", "appium"]
Framework = Literal["selenium", "playwright", "cypress", "appium", "testng", "junit"]


class SelectionPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        # --- Radio: Gender ---
        self._gender_group = page.get_by_test_id("gender-radios")
        self._gender_output_label = page.get_by_test_id("gender-output")

        # --- Checkboxes: Skills ---
        self._skills_group = page.get_by_test_id("skills-checkboxes")
        self._skills_output_label = page.get_by_test_id("skills-output")

        # --- Multi Select (native) ---
        self._country_select = page.get_by_test_id("country-select")
        self._country_output_label = page.get_by_test_id("country-output")

        # --- Multi Select Listbox (Native) ---
        self._languages_select = page.get_by_test_id("languages-select")
        self._languages_output_label = page.get_by_test_id("languages-output")

        # --- Multi Select Dropdown ---
        self._frameworks_trigger = page.get_by_test_id("frameworks-multi-select-trigger")
        self._frameworks_panel = page.get_by_test_id("frameworks-multi-select-panel")
        self._frameworks_value = page.get_by_test_id("frameworks-multi-select-value")
        self._frameworks_output_label = page.get_by_test_id("frameworks-multi-output")

        # --- Experience (Range Slider) ---
        self._experience_range = page.get_by_test_id("experience-range")
        self._experience_output_label = page.get_by_test_id("experience-output")

        # --- Color Picker ---
        self._color_input = page.get_by_test_id("color-input")
        self._color_output_label = page.get_by_test_id("color-output")

        # --- Notifications (Toggle) ---
        self._toggle_notifications_checkbox = page.get_by_test_id("toggle-notifications")
        self._toggle_output_label = page.get_by_test_id("toggle-output")

        # --- Auto-complete Input ---
        self._autocomplete_input = page.get_by_test_id("autocomplete-input")
        self._autocomplete_suggestions = page.get_by_test_id("autocomplete-suggestions")
        self._autocomplete_output_label = page.get_by_test_id("autocomplete-output")


    def open(self) -> None:
        super().open("#selection")

    def get_gender_output(self) -> Locator:
        return self._gender_output_label

    def get_skills_output(self) -> Locator:
        return self._skills_output_label

    def get_country_output(self) -> Locator:
        return self._country_output_label

    def get_languages_output(self) -> Locator:
        return self._languages_output_label

    def get_frameworks_output(self) -> Locator:
        return self._frameworks_output_label

    def get_experience_output(self) -> Locator:
        return self._experience_output_label

    def get_color_output(self) -> Locator:
        return self._color_output_label

    def get_toggle_output(self) -> Locator:
        return self._toggle_output_label

    def get_autocomplete_output(self) -> Locator:
        return self._autocomplete_output_label

    def select_gender(self, gender: Gender) -> None:
        self._gender_group.get_by_test_id(f"gender-{gender.lower()}").check()

    def select_skill(self, skill: Skill) -> None:
        self.page.get_by_test_id(f"skill-{skill}").check()

    def select_country_by_text(self, text: str) -> None:
        self._country_select.select_option(text)

    def select_languages(self, *values: str) -> None:
        self._languages_select.select_option(list(values))

    def open_frameworks_dropdown(self) -> None:
        if self._frameworks_panel.is_hidden():
            self._frameworks_trigger.click()

    def close_frameworks_dropdown(self) -> None:
        if self._frameworks_panel.is_visible():
            self._frameworks_trigger.click()

    def select_frameworks(self, *frameworks: Framework) -> None:
        self.open_frameworks_dropdown()
        for fw in frameworks:
            self.page.get_by_test_id(f"framework-{fw}").check()
        self.close_frameworks_dropdown()

    def unselect_frameworks(self, *frameworks: Framework) -> None:
        self.open_frameworks_dropdown()
        for fw in frameworks:
            self.page.get_by_test_id(f"framework-{fw}").uncheck()
        self.close_frameworks_dropdown()

    def set_experience(self, years: int) -> None:
        self._experience_range.fill(str(years))

    def set_color(self, hex_color: str) -> None:
        self._color_input.fill(hex_color)

    def toggle_notifications(self) -> None:
        if not self.is_notifications_enabled():
            self._toggle_notifications_checkbox.check(force=True)
        else:
            self._toggle_notifications_checkbox.uncheck(force=True)

    def is_notifications_enabled(self) -> bool:
        return self._toggle_notifications_checkbox.is_checked()

    def type_autocomplete(self, text: str) -> None:
        self._autocomplete_input.fill(text)

    def select_autocomplete_suggestion(self, text: str) -> None:
        self._autocomplete_suggestions.get_by_role("option", name=text).click()
