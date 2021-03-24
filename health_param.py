import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def health_pa(name,birth,pw):
    brow = webdriver.Chrome()
    brow.maximize_window()

    brow.get('https://hcs.eduro.go.kr/')

    # 자가진다 버튼 클릭
    elem = brow.find_element_by_xpath('//*[@id="btnConfirm2"]')
    elem.click()

    elem = brow.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[1]/td/button')
    elem.click()
    # 대구광역시 클릭
    elem = brow.find_element_by_xpath('//*[@id="sidolabel"]/option[4]')
    elem.click()
    # 고등학교 클릭
    brow.find_element_by_xpath('//*[@id="crseScCode"]/option[5]').click()

    elem = brow.find_element_by_xpath('//*[@id="orgname"]')
    elem.send_keys('소프트웨어')
    elem.send_keys(Keys.ENTER)

    time.sleep(1)   # 소프트웨어 검색 하고 나서 바로 안뜰수도 있어서 1초 쉼.

    brow.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p').click()
    brow.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()
    #이름넣기
    elem = brow.find_element_by_xpath('//*[@id="user_name_input"]')
    elem.send_keys(name)

    #생년월일 넣기
    brow.find_element_by_xpath('//*[@id="birthday_input"]').send_keys(birth)
    brow.find_element_by_xpath('//*[@id="btnConfirm"]').click()

    time.sleep(2)

    #비밀번호 넣기
    brow.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/input').send_keys(pw)
    brow.find_element_by_xpath('//*[@id="btnConfirm"]').click()

    # 이름 생년월일 비밀번호 사용자 입력받는거...

    time.sleep(4)
    brow.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a/span[1]').click()
    time.sleep(2)
    brow.find_element_by_xpath('//*[@id="survey_q1a1"]').click()
    brow.find_element_by_xpath('//*[@id="survey_q2a1"]').click()
    brow.find_element_by_xpath('//*[@id="survey_q3a1"]').click()
    brow.find_element_by_xpath('//*[@id="btnConfirm"]').click()

    time.sleep(5)
    brow.quit()