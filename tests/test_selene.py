import allure
from allure_commons.types import Severity
from selene import be, by
from selene.support.shared import browser


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Gavrichenkova Anastasia")
@allure.feature("Search")
@allure.story("Search a repository and an check issue into it")
@allure.link("https://github.com", name="Testing")
def test_search_selene():
    browser.open('https://github.com')

    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').submit()

    browser.element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text('#74')).should(be.visible)
