import allure
import pytest
from playwright.sync_api import Page, BrowserContext
from pages.base_page import BasePage

@pytest.fixture
def base_page(page: Page) -> BasePage:
    return BasePage(page)

@pytest.fixture(autouse=True)
def screenshot_on_failure(context: BrowserContext, request):
    yield

    if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
        for i, p in enumerate(context.pages):
            if not p.is_closed():
                allure.attach(p.screenshot(full_page=True),
                              name=f"Screenshot on failure #{i}",
                              attachment_type=allure.attachment_type.PNG)
