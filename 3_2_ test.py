from selene import be, have
from selene.support.shared import browser


def test_sl1(br_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_sl2(br_size1):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.no.text('условие задачи понято не верно'))


def test_sl3():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('sdfq12wdqsdfsdfsdfsdfsdf').press_enter()
    browser.element('[id="result-stats"]').should(have.text("Результатов: примерно 0"))
