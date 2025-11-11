import pytest
from playwright.sync_api import sync_playwright, expect, Playwright, Page


@pytest.fixture(scope="session")
def initialize_browser_state():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Ввод данных в форму
        email_field = page.get_by_test_id("registration-form-email-input").locator('input')
        email_field.fill("user.name@gmail.com")
        username_field = page.get_by_test_id("registration-form-username-input").locator('input')
        username_field.fill("username")
        password_field = page.get_by_test_id("registration-form-password-input").locator('input')
        password_field.fill("password")
        page.get_by_test_id("registration-page-registration-button").click()

        # Сохранение состояния браузера в JSON
        context.storage_state(path="browser-state.json")

        # Проверка перехода на страницу Dashboard после регистрации
        dashboard_title_text = page.get_by_test_id("dashboard-toolbar-title-text")
        expect(dashboard_title_text).to_have_text("Dashboard")


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    yield page
    page.close()
