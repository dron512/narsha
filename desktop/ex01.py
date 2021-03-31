import pyautogui
import time

pos = pyautogui.position()
print('x = ',pos.x,'y = ',pos.y)

time.sleep(1)
pyautogui.click(100,38,duration=2)

# pyautogui.moveTo(1770,820)
# pyautogui.moveTo(100,200,duration=2)

# pyautogui.move(100,100,duration=2)
# pyautogui.move(100,100,duration=2)
# pyautogui.move(100,100,duration=2)


# def mydoa(a,b,c):
#     print("a",a)
#     print("b",b)
#     print("c",c)

# mydoa(10,c=20,b=30)


# size = pyautogui.size()
# print("size[0]",size[0])
# print(size[1])

# width,height = pyautogui.size()
# print(width)
# print(height)