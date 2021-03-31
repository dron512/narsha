import pyautogui as py
import pyperclip as pc
import time

time.sleep(1)

py.hotkey('win','r')
py.write('notepad')
time.sleep(1)
py.hotkey('enter')

# 컴퓨터.. 전기.. 기계... 용접.. 자동차... 화학...토목... 건축..
def copypa(text):
    pc.copy(text)
    py.hotkey('ctrl','v')

copypa('한글한글한글')