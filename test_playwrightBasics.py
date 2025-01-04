import time
from pydoc import pager

from playwright.sync_api import Page, Playwright


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")
    time.sleep(5)



def test_playwrightShortcut(page:Page):
    page.goto("https://www.makemytrip.com")
    time.sleep(5)

def test_loginTest(page:Page):
    page.goto("https://www.rahulshettyacademy.com/")


def test_core_Locator(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    time.sleep(5)
    page.get_by_role('link', name='terms and conditions').click()
    page.get_by_role('button', name='Sign in').click()
    time.sleep(5)

def test_firefoxtest(playwright : Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    time.sleep(5)
    page.get_by_role('link', name='terms and conditions').click()
    page.get_by_role('button', name='Sign in').click()
    time.sleep(5)
