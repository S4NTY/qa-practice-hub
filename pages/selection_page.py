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
        self.gender_group = page.get_by_test_id("gender-radios")
        self.gender_output_label = page.get_by_test_id("gender-output")

        # --- Checkboxes: Skills ---
        self.skills_group = page.get_by_test_id("skills-checkboxes")
        self.skills_output_label = page.get_by_test_id("skills-output")

        # --- Multi Select (native) ---
        self.country_select = page.get_by_test_id("country-select")
        self.country_output_label = page.get_by_test_id("country-output")

        # --- Multi Select Listbox (Native) ---
        self.languages_select = page.get_by_test_id("languages-select")
        self.languages_output_label = page.get_by_test_id("languages-output")

        # --- Multi Select Dropdown ---
        self.frameworks_trigger = page.get_by_test_id("frameworks-multi-select-trigger")
        self.frameworks_panel = page.get_by_test_id("frameworks-multi-select-panel")
        self.frameworks_value = page.get_by_test_id("frameworks-multi-select-value")
        self.frameworks_output_label = page.get_by_test_id("frameworks-multi-output")

        # --- Experience (Range Slider) ---
        self.experience_range = page.get_by_test_id("experience-range")
        self.experience_output_label = page.get_by_test_id("experience-output")

        # --- Color Picker ---
        self.color_input = page.get_by_test_id("color-input")
        self.color_output_label = page.get_by_test_id("color-output")

        # --- Notifications (Toggle) ---
        self.toggle_notifications_checkbox = page.get_by_test_id("toggle-notifications")
        self.toggle_output_label = page.get_by_test_id("toggle-output")

        # --- Auto-complete Input ---
        self.autocomplete_input = page.get_by_test_id("autocomplete-input")
        self.autocomplete_suggestions = page.get_by_test_id("autocomplete-suggestions")
        self.autocomplete_output_label = page.get_by_test_id("autocomplete-output")


    def open(self) -> None:
        super().open("#selection")

    def get_gender_output(self) -> Locator:
        return self.gender_output_label

    def get_skills_output(self) -> Locator:
        return self.skills_output_label

    def get_country_output(self) -> Locator:
        return self.country_output_label

    def get_languages_output(self) -> Locator:
        return self.languages_output_label

    def get_frameworks_output(self) -> Locator:
        return self.frameworks_output_label

    def get_experience_output(self) -> Locator:
        return self.experience_output_label

    def get_color_output(self) -> Locator:
        return self.color_output_label

    def get_toggle_output(self) -> Locator:
        return self.toggle_output_label

    def get_autocomplete_output(self) -> Locator:
        return self.autocomplete_output_label

    def select_gender(self, gender: Gender) -> None:
        self.gender_group.get_by_test_id(f"gender-{gender.lower()}").check()

    def select_skill(self, skill: Skill) -> None:
        self.page.get_by_test_id(f"skill-{skill}").check()

    def select_country_by_text(self, text: str) -> None:
        self.country_select.select_option(text)

    def select_languages(self, *values: str) -> None:
        self.languages_select.select_option(list(values))

    def open_frameworks_dropdown(self) -> None:
        if self.frameworks_panel.is_hidden():
            self.frameworks_trigger.click()

    def close_frameworks_dropdown(self) -> None:
        if self.frameworks_panel.is_visible():
            self.frameworks_trigger.click()

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
        self.experience_range.fill(str(years))

    def set_color(self, hex_color: str) -> None:
        self.color_input.fill(hex_color)

    def toggle_notifications(self) -> None:
        if not self.is_notifications_enabled():
            self.toggle_notifications_checkbox.check(force=True)
        else:
            self.toggle_notifications_checkbox.uncheck(force=True)

    def is_notifications_enabled(self) -> bool:
        return self.toggle_notifications_checkbox.is_checked()

    def type_autocomplete(self, text: str) -> None:
        self.autocomplete_input.fill(text)

    def select_autocomplete_suggestion(self, text: str) -> None:
        self.autocomplete_suggestions.get_by_role("option", name=text).click()
