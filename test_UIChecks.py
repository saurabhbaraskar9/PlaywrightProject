import time

from playwright.sync_api import Page, expect


def test_UIHandling(page:Page):
    page.goto('https://rahulshettyacademy.com/AutomationPractice/')
    expect(page.get_by_placeholder('Hide/Show Example')).to_be_visible()
    page.get_by_role('button', name='Hide').click()
    expect(page.get_by_placeholder('Hide/Show Example')).to_be_hidden()

def test_alertHandling(page:Page):
    page.goto('https://rahulshettyacademy.com/AutomationPractice/')
    time.sleep(3)
    page.on('dialog', lambda dialog:dialog.accept())
    page.get_by_role('button', name='Confirm').click()
    time.sleep(5)

def test_FrameHandling(page:Page):
    page.goto('https://rahulshettyacademy.com/AutomationPractice/')
    pageframe = page.frame_locator('#courses-iframe')
    pageframe.get_by_role('link', name='All Access plan').click()
    expect(pageframe.locator(('body'))).to_contain_text('Happy Subscibers!')