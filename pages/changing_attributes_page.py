from pages.base_page import BasePage
from playwright.sync_api import Locator, Page


class ChangingAttributesPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.pause_button = page.get_by_test_id("btn-attrs-pause")
        self.resume_button = page.get_by_test_id("btn-attrs-resume")
        self.reset_button = page.get_by_test_id("btn-attrs-reset")
        self.speed_select = page.get_by_test_id("attrs-speed")
        self.timer_state = page.get_by_test_id("attrs-timer-state")
        self.clock_button = page.get_by_test_id("attrs-clock-btn")
        self.status_badge = page.get_by_test_id("attrs-status-badge")
        self.status_output = page.get_by_test_id("attrs-status-output")
        self.flip_id_input = page.get_by_test_id("flip-id-input")
        self.flip_id_readout = page.get_by_test_id("flip-id-readout")
        self.countdown_button = page.get_by_test_id("attrs-countdown-btn")
        self.countdown_output = page.get_by_test_id("attrs-countdown-output")
        self.mutating_link = page.get_by_test_id("attrs-mutating-link")
        self.link_readout = page.get_by_test_id("attrs-link-readout")


    def open(self) -> None:
        super().open("#changing-attrs")

    def get_timer_state(self) -> Locator:
        return self.timer_state

    def get_speed_select(self) -> Locator:
        return self.speed_select

    def get_clock_button(self) -> Locator:
        return self.clock_button

    def get_status_badge(self) -> Locator:
        return self.status_badge

    def get_status_output(self) -> Locator:
        return self.status_output

    def get_flip_id_input(self) -> Locator:
        return self.flip_id_input

    def get_flip_id_readout(self) -> Locator:
        return self.flip_id_readout

    def get_countdown_button(self) -> Locator:
        return self.countdown_button

    def get_countdown_output(self) -> Locator:
        return self.countdown_output

    def get_mutating_link(self) -> Locator:
        return self.mutating_link

    def get_link_readout(self) -> Locator:
        return self.link_readout

    def pause_timers(self) -> None:
        self.pause_button.click()

    def resume_timers(self) -> None:
        self.resume_button.click()

    def reset_widgets(self) -> None:
        self.reset_button.click()

    def set_speed(self, speed: str) -> None:
        self.speed_select.select_option(speed)

    def click_status_badge(self) -> None:
        self.status_badge.click()

    def click_countdown_button(self) -> None:
        self.countdown_button.click()

    def click_mutating_link(self) -> None:
        self.mutating_link.click()