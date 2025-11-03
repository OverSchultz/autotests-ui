from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
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


    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Проверка наличия блоков
        course_title_text = page.get_by_test_id("courses-list-toolbar-title-text")
        expect(course_title_text).to_be_visible()
        expect(course_title_text).to_have_text("Courses")

        courses_empty_view_text = page.get_by_test_id("courses-list-empty-view-title-text")
        expect(courses_empty_view_text).to_be_visible()
        expect(courses_empty_view_text).to_have_text("There is no results")

        courses_empty_view_icon = page.get_by_test_id("courses-list-empty-view-icon")
        expect(courses_empty_view_icon).to_be_visible()

        courses_empty_description_text = page.get_by_test_id("courses-list-empty-view-description-text")
        expect(courses_empty_description_text).to_be_visible()
        expect(courses_empty_description_text).to_have_text("Results from the load test pipeline will be displayed here")



