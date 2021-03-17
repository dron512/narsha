import time
from selenium import webdriver

brow = webdriver.Chrome()
brow.maximize_window()

brow.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

brow.switch_to.frame('iframeResult')

elem = brow.find_element_by_xpath('//*[@id="male"]')

if elem.is_selected() == False:
    print("선택 안되어 있으므로 선택")
    elem.click()
else :
    print("이미 선택 되어 있습니다.")

time.sleep(5)
brow.quit()