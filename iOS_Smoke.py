import os
import pytest
from time import sleep
from appium import webdriver

desired_caps = {
'platformName': 'iOS',
'platformVersion': '14.3',
'deviceName': 'iPhone 8',
'app': '/Users/romanchichiro/Downloads/ADSirius-14.app'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

# Steps:
email = driver.find_element_by_accessibility_id('emailInput')
email.send_keys('alpinapublisher@bm.fbl.su')
password = driver.find_element_by_accessibility_id('passwordInput')
password.send_keys('123qwe')
log_in = driver.find_element_by_accessibility_id('loginButton')
log_in.click()
choise_offer = driver.find_element_by_accessibility_id('Холдинг «Альпина»')
choise_offer.click()
next_button = driver.find_element_by_ios_class_chain('**/XCUIElementTypeButton[`label == "NEXT"`]')
next_button.click()
pop_up_notification_allow = driver.find_element_by_accessibility_id('Allow')
pop_up_notification_allow.click()
changing_icon = driver.find_element_by_accessibility_id('OK')
changing_icon.click()
showing_book_atlant = driver.find_element_by_accessibility_id('Атлант расправил плечи (3 тома)')
sleep(1)
driver.quit()