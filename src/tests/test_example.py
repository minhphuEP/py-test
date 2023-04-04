import pytest
from playwright.sync_api import Playwright, Browser, BrowserContext, Page

@pytest.fixture(scope="module")
def playwright() -> Playwright:
    from playwright.sync_api import Playwright
    with Playwright() as playwright:
        yield playwright

@pytest.fixture(scope="module")
def browser(playwright: Playwright, request: pytest.FixtureRequest) -> Browser:
    browser_name = request.config.getoption("--browser")
    if browser_name == "chromium":
        browser_type = playwright.chromium
    elif browser_name == "firefox":
        browser_type = playwright.firefox
    else:
        raise ValueError(f"Invalid browser name: {browser_name}")
    browser = browser_type.launch(headless=True)
    yield browser
    browser.close()

def test_example(browser: Browser):
    with browser.new_context() as context:
        page = context.new_page()
        page.goto("https://example.com")
        assert page.title() == "Example Domain"

def test_parallel(browser: Browser):
    with browser.new_context() as context:
        page = context.new_page()
        page.goto("https://example.com")
        assert page.title() == "Example Domain"
