from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

browser.get('http://www.naver.com')

webton=browser.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[9]/a')
href = webton.get_attribute('href')

# webton.click()

input_sear = browser.find_element_by_id('query')
input_sear.send_keys('python')

input_sear.send_keys(Keys.ENTER)

# elem = browser.find_element_by_link_text('프리미엄\
#      코딩교육 위즈라이브')
# elem.click()

elems = browser.find_elements_by_tag_name('a')
for e in elems :
    # print("test")
    print(e.get_attribute('href'))

browser.save_screenshot("naver_python.png")

time.sleep(5)

browser.close()
browser.quit()