from selene.support.shared import browser
from selene import be, have


def br_size(a, b):
    browser.config.window_width = a
    browser.config.window_height = b


def test_sl1():
    br_size(800, 600)
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_sl2():
    br_size(1024, 800)
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('selenoid: User-oriented Web UI browser tests in Python'))
