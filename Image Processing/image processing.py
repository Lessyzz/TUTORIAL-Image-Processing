#bylessy

#game url: "https://gamesge.com/en/whack-a-mole/"
#i'm not supporting hacking, just i show how to running image processing ^^

from email.mime import image
from python_imagesearch.imagesearch import imagesearch
import pyautogui
from pynput.mouse import Button, Controller
import time

mouse = Controller()
time.sleep(5) #Waiting for the game to open when the script runs
while True:
    mole_noseboss = imagesearch("your location/imageprocessing/molenoseboss.png") #you need to change location
    #for example >>>> imagesearch("C:/user/Desktop/imageprocessing/molenoseboss.png")
    if mole_noseboss[0] != -1:
        print("Boss nose found") #Click the mose's nose >>> [0] = X , [1] = Y 
        pyautogui.click(mole_noseboss[0] , mole_noseboss[1]+30)
        pyautogui.click(mole_noseboss[0] , mole_noseboss[1]+30)
        pyautogui.click(mole_noseboss[0] , mole_noseboss[1]+30)
        pyautogui.click(mole_noseboss[0] , mole_noseboss[1]+30)
        pyautogui.click(mole_noseboss[0] , mole_noseboss[1]+30)
        pyautogui.click(mole_noseboss[0] , mole_noseboss[1]+30)

    mole_nosethree = imagesearch("your location/imageprocessing/molenosethree.png") #you need to change location
    #for example >>>> imagesearch("C:/user/Desktop/imageprocessing/molenosethree.png")
    if mole_nosethree[0] != -1:
        print("Boss nose found") #Click the mose's nose >>> [0] = X , [1] = Y 
        pyautogui.click(mole_nosethree[0] , mole_nosethree[1])
        pyautogui.click(mole_nosethree[0] , mole_nosethree[1])
        pyautogui.click(mole_nosethree[0] , mole_nosethree[1])

    mole_nose = imagesearch("your location/imageprocessing/molenose.png") #you need to change location
    #for example >>>> imagesearch("C:/user/Desktop/imageprocessing/molenose.png")
    if mole_nose[0] != -1: #Scanning the mole's nose in the screen
        print("Nose found") #Click the mose's nose >>> [0] = X , [1] = Y 
        mouse.position = (mole_nose[0] , mole_nose[1])
        mouse.press(Button.left)
        time.sleep(0.1)
        mouse.release(Button.left)
    else:
        pass

#end