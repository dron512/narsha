import pyautogui
import time

# UTC 똑똑한 사람들 1970년 1월1일.. 시간을 초단위.. 만들자고..
def find_img(img,timeout=30):
    start = time.time()
    print("start",start)
    print("timeout",timeout)
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img)
        end = time.time()
        if end - start > timeout:
            break
    return target

target = find_img('file.PNG')
pyautogui.click(target)
print(target)

# img = pyautogui.screenshot()
# img.save('a.png')

# view_menu = pyautogui.locateOnScreen('view_menu.png')
# print(view_menu)
# pyautogui.click(view_menu,duration=2)

#     print(vi)
# for vi in pyautogui.locateAllOnScreen('view_menu.png'):