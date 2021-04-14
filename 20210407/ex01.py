import pyautogui
import time
from copyhan import Han
# from copyhan import docp

#윈도우 r 조합해서 누르는거
pyautogui.hotkey('win','r')
#mspaint 입력
pyautogui.write('mspaint')
#enter키 입력
pyautogui.press('enter')

#2초 쉬기
time.sleep(2)
window = pyautogui.getWindowsWithTitle('제목 없음 - 그림판')[0]
window.maximize()

# 그림 이미지의 픽셀이 80%만 같아도 box 찾아서 넣어줌...
box = pyautogui.locateOnScreen('font.PNG')
# print(box)    좌표랑... 넓이높이...
pyautogui.click(box,duration=2)

'''
    moveTo 절대 좌표 왼쪽 위에가 0,0
    move 상대좌표 
'''
pyautogui.move(0,200,duration=2)
pyautogui.click()

# 생성자 호출해서 클래스 메모리화...
han = Han()
han.docp(text='한글잘됨')

pyautogui.hotkey('ctrl','v')

# pyautogui.write('basdfasdf')
# pyautogui.write('한글')

time.sleep(5)
window.close()
pyautogui.press('n')

# pip install pyautogui pyautogui 설치