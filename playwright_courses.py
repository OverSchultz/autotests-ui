from playwright.sync_api import sync_playwright, expect


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

    button_registration = page.get_by_test_id("registration-page-registration-button").click()


    # Сохранение состояния браузера в JSON
    context.storage_state(path="browser-state.json")


    # Проверка перехода на страницу Dashboard после регистрации
    title_dashboard = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(title_dashboard).to_have_text("Dashboard")



with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")


    # Проверка наличия блоков
    # P.S.  Добавил проверку на видимость, хотя проверки на текст достатчоно.
    #       Но по заданию два условия
    course_text = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(title_dashboard).to_be_visible()
    expect(title_dashboard).to_have_text("Courses")

    block_text = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(block_text).to_be_visible()
    expect(block_text).to_have_text("There is no results")

    check_empty_icon = page.get_by_test_id("courses-list-empty-view-icon")
    expect(check_empty_icon).to_be_visible()

    check_block_description = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(check_block_description).to_be_visible()
    expect(check_block_description).to_have_text("Results from the load test pipeline will be displayed here")



