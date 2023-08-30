from selene import be, by
from selene.support.shared import browser


def test_search_selene():
    browser.open('https://github.com')

    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').submit()

    browser.element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text('#74')).should(be.visible)
