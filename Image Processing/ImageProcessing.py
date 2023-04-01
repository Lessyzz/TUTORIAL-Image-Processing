# Game url: "https://gamesge.com/en/whack-a-mole/"

from python_imagesearch.imagesearch import imagesearch
import pyautogui, os, sys

class ImageProcessing:
    def __init__(self):
        # Get current path
        if getattr(sys, "frozen", False):
            self.PATH = os.path.dirname(sys.executable)
        elif __file__:
            self.PATH = os.path.dirname(__file__)

        self.image = self.PATH + "/molenose.png"
        self.bang()

    def bang(self):
        while True:
            if ((mole := imagesearch(self.image)))[0] != -1:
                pyautogui.leftClick(mole[0], mole[1])

Run = ImageProcessing()
