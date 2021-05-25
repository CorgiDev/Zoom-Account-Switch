import os
import pandas as pd
import pyautogui
import time

import settings

#Open's Zoom Application from the specified location
def openZoom ():
    os.startfile(settings.startfile)
    time.sleep(3)

#Join a meeting once logged in
#def joinMeeting():