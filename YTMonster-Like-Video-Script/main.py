import pyautogui
import time

time.sleep(2)
#Locate an image on the screen
while True:
    located = False
    while not located:
        location = pyautogui.locateOnScreen('like.png')
        print("Locating image...")
        if location != None:
            located = True
            print("Image located!")
    #Move the mouse to the center of the image
    pyautogui.moveTo(location)
    #Click on the image
    pyautogui.click()
    #Locate another image
    located = False
    while not located:
        newLocation = pyautogui.locateOnScreen('YTLike.png')
        print("Locating YTLike image...")
        if newLocation != None:
            located = True
            print("YTLike image located!")
    #Move the mouse to the center of the image
    pyautogui.moveTo(newLocation)
    #Click on the image
    pyautogui.click()
    time.sleep(22)
    pyautogui.hotkey('ctrl', '1')
    for i in range(1,5):
        latestLocation = pyautogui.locateOnScreen('verify.png')
        time.sleep(1)
    pyautogui.moveTo(latestLocation)
    pyautogui.click()
    verifying = True
    while verifying:
        if pyautogui.locateOnScreen('verifying.png') == None:
            verifying = False
        else:
            verifying=True
    