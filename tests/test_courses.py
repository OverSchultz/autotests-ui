

from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверка наличия блоков
    course_title_text = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(course_title_text).to_be_visible()
    expect(course_title_text).to_have_text("Courses")

    courses_empty_view_text = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(courses_empty_view_text).to_be_visible()
    expect(courses_empty_view_text).to_have_text("There is no results")

    courses_empty_view_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(courses_empty_view_icon).to_be_visible()

    courses_empty_description_text = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(courses_empty_description_text).to_be_visible()
    expect(courses_empty_description_text).to_have_text("Results from the load test pipeline will be displayed here")
