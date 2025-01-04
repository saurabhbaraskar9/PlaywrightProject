import time

from playwright.async_api import Page
from playwright.sync_api import expect


def test_UIDynamicvalidations(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    time.sleep(5)
    # page.get_by_role('link', name='terms and conditions').click()
    page.locator('#terms').check()
    page.get_by_role('button', name='Sign in').click()
    time.sleep(5)
    iphone = page.locator('app-card').filter(has_text='iphone X')
    iphone.get_by_role('button').click()
    Nokia = page.locator('app-card').filter(has_text='Nokia Edge')
    Nokia.get_by_role('button').click()
    time.sleep(5)
    page.get_by_text('Checkout').click()
    time.sleep(5)
    expect(page.locator('.media-body')).to_have_count(2)