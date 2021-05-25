import os
import pandas as pd
import json
import pyautogui
import time
from datetime import datetime

import settings
import secrets

def signIn(accountSelected):

    # Read Account JSON file
    df = pd.read_excel('secrets.xlsx',index=False)

    # Spit out list of accounts

    # Ask user to select an account

    # Retrieve password for selected account

    # Set password and username values
    email = ""
    password = secrets.retrieveSecret().secret

    #Click the Sign In button
    pyautogui.moveTo(settings.signinBtn)
    pyautogui.click()
    time.sleep(1)

    #Enter's Email Address for Account
    pyautogui.moveTo(settings.signinEmailfield)
    pyautogui.write(email)
    time.sleep(1)

    #Enter's Password for Account
    pyautogui.moveTo(settings.signinPasswordfield)
    pyautogui.write(password)
    time.sleep(1)

    #Click's the sign in confirmation button
    pyautogui.moveTo(settings.signinConfirmBtn)
    pyautogui.click()
    time.sleep(1)