from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    browser.get("https://alpinapublisher.addev.alpinadigital.ru")
    browser.fullscreen_window()
    time.sleep(2) # пауза для демонстрации содержимого экрана

    login = browser.find_element(By.NAME, "email")
    login.send_keys("alpinapublisher@bm.fbl.su")

    password = browser.find_element(By.NAME, "password")
    password.send_keys("123qwe")

    time.sleep(2) # пауза для демонстрации содержимого экрана

    logging = browser.find_element(By.CLASS_NAME, "btn.short")
    logging.click()

    time.sleep(4) # пауза для демонстрации содержимого экрана

    profile = browser.find_element(By.LINK_TEXT, "alpinapublisher")
    profile.click()

    account_name = browser.find_element(By.XPATH, "//span[contains(text(),'alpinapublisher')]")
    account_name_text = account_name.text
    # print(account_name_text)

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "alpinapublisher" == account_name_text

    time.sleep(2) # пауза для демонстрации содержимого экрана

    logout = browser.find_element(By.CLASS_NAME, "logout")
    logout.click()

finally:
    time.sleep(4) # пауза для демонстрации содержимого экрана
    browser.quit()
