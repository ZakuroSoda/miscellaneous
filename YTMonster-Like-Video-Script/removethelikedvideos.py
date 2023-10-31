import pyautogui
from time import sleep

sleep(2)
located = False
while not located:
    location = pyautogui.locateOnScreen("threedots.png")
    if location != None:
        located = True
times = 0
for i in range(0,times):
    pyautogui.moveTo(location)
    #Click on the image
    pyautogui.click()
    location2 = pyautogui.locateOnScreen("remove.png")
    pyautogui.moveTo(location2)
    pyautogui.click()