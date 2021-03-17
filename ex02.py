import time
from selenium import webdriver

brow = webdriver.Chrome()
brow.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

brow.switch_to.frame("iframeResult")

elem = brow.find_element_by_xpath('//*[@id="male"]')
elem.click()

time.sleep(5)

print("5초뒤에 출력됨")

brow.quit() # 종료됨...