import os
import pandas as pd
import pyautogui
import time
from datetime import datetime

import settings
#import zoomFunctions as zf

# Open Zoom
os.startfile(settings.startfile)
time.sleep(3)

# Check if already logged in
#zf.confirmLogin

# If logged in, 
    # List what account you are logged in with
    # Verify you wish to remain logged in
    # If you do, close app.
    # If you don't log out

# If not logged in,
    # List accounts available
    # Select account you wish to login with
    # Login

# Login to a meeting
    # Verify logged in
    # Take in information needed to join meeting