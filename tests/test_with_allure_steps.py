import allure
from selene import be, by
from selene.support.shared import browser


def test_search_selene():
    with allure.step('Open the main page'):
        browser.open('https://github.com')

    with allure.step('Search for repository'):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').submit()

    with allure.step('Open the repository'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Open the Issue tab'):
        browser.element('#issues-tab').click()

    with allure.step('Check the Issue number 74'):
        browser.element(by.partial_text('#74')).should(be.visible)
