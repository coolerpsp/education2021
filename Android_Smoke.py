from appium import webdriver
from time import sleep

desired_caps = {
"platformName": "Android",
"platformVersion": "8.1",
"deviceName": "Pixel_2_XL_API_275",
"app": "/Users/romanchichiro/Downloads/singleapp-3.apk",
"avd": "Pixel_2_XL_API_27"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(40)

email = driver.find_element_by_id('ru.alpina.singleapp:id/loginEmailEditText')
email.send_keys('alpinapublisher@bm.fbl.su')
next1 = driver.find_element_by_id('ru.alpina.singleapp:id/loginNextBtn').click()
next2 = driver.find_element_by_id('ru.alpina.singleapp:id/loginEnterPassword').click()
password = driver.find_element_by_id('ru.alpina.singleapp:id/loginPasswordEditText')
password.send_keys('123qwe')
next3 = driver.find_element_by_id('ru.alpina.singleapp:id/loginEnterBtn').click()
sleep(3)
choise_offer = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]').click()
showing_book_item = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[1]')
sleep(3)
#assert int(numbers_field.text) == 10
driver.quit()