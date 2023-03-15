# Game url: "https://gamesge.com/en/whack-a-mole/"

from python_imagesearch.imagesearch import imagesearch
import pyautogui, os, sys

if getattr(sys, "frozen", False): # Getting current path
    PATH = os.path.dirname(sys.executable)
elif __file__:
    PATH = os.path.dirname(__file__)

class ImageProcessing:
    def __init__(self):
        self.image = PATH + "/molenose.png"
        self.bang()

    def bang(self):
        while True:
            if ((mole := imagesearch(self.image)))[0] != -1:
                pyautogui.leftClick(mole[0], mole[1])

Run = ImageProcessing()
