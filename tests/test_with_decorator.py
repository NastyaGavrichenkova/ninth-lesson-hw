import allure
from selene import be, by
from selene.support.shared import browser


@allure.step('Open the main page')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Search for repository {repo}')
def search_for_repository(repo):
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').send_keys(repo).submit()


@allure.step('Open the repository {repo}')
def open_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Open the Issue tab')
def open_issues_tab():
    browser.element('#issues-tab').click()


@allure.step('Check the Issue number {number}')
def check_issue_number(number):
    browser.element(by.partial_text(number)).should(be.visible)


def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    open_repository("eroshenkoam/allure-example")
    open_issues_tab()
    check_issue_number("#74")
