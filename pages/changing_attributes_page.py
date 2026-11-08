from pages.base_page import BasePage
from playwright.sync_api import Locator, Page


class ChangingAttributesPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._pause_button = page.get_by_test_id("btn-attrs-pause")
        self._resume_button = page.get_by_test_id("btn-attrs-resume")
        self._reset_button = page.get_by_test_id("btn-attrs-reset")
        self._speed_select = page.get_by_test_id("attrs-speed")
        self._timer_state = page.get_by_test_id("attrs-timer-state")
        self._clock_button = page.get_by_test_id("attrs-clock-btn")
        self._status_badge = page.get_by_test_id("attrs-status-badge")
        self._status_output = page.get_by_test_id("attrs-status-output")
        self._flip_id_input = page.get_by_test_id("flip-id-input")
        self._flip_id_readout = page.get_by_test_id("flip-id-readout")
        self._countdown_button = page.get_by_test_id("attrs-countdown-btn")
        self._countdown_output = page.get_by_test_id("attrs-countdown-output")
        self._mutating_link = page.get_by_test_id("attrs-mutating-link")
        self._link_readout = page.get_by_test_id("attrs-link-readout")


    def open(self) -> None:
        super().open("#changing-attrs")

    def get_timer_state(self) -> Locator:
        return self._timer_state

    def get_speed_select(self) -> Locator:
        return self._speed_select

    def get_clock_button(self) -> Locator:
        return self._clock_button

    def get_status_badge(self) -> Locator:
        return self._status_badge

    def get_status_output(self) -> Locator:
        return self._status_output

    def get_flip_id_input(self) -> Locator:
        return self._flip_id_input

    def get_flip_id_readout(self) -> Locator:
        return self._flip_id_readout

    def get_countdown_button(self) -> Locator:
        return self._countdown_button

    def get_countdown_output(self) -> Locator:
        return self._countdown_output

    def get_mutating_link(self) -> Locator:
        return self._mutating_link

    def get_link_readout(self) -> Locator:
        return self._link_readout

    def pause_timers(self) -> None:
        self._pause_button.click()

    def resume_timers(self) -> None:
        self._resume_button.click()

    def reset_widgets(self) -> None:
        self._reset_button.click()

    def set_speed(self, speed: str) -> None:
        self._speed_select.select_option(speed)

    def click_status_badge(self) -> None:
        self._status_badge.click()

    def click_countdown_button(self) -> None:
        self._countdown_button.click()

    def click_mutating_link(self) -> None:
        self._mutating_link.click()