import os
import pandas as pd
import pyautogui

#Program File Locations
startfile = "C:\Program Files (x86)\Zoom\bin\Zoom.exe"

#Button Image Assets
joinbtn=pyautogui.locateCenterOnScreen("")
meetingidbtn=pyautogui.locateCenterOnScreen("")
mediaBtn=pyautogui.locateAllOnScreen("")
join=pyautogui.locateCenterOnScreen("")
passcode=pyautogui.locateCenterOnScreen("")
joinmeeting=pyautogui.locateCenterOnScreen("")
signinEmailfield = pyautogui.locateCenterOnScreen("assets\accountEmailField.PNG")
signinPasswordfield = pyautogui.locateCenterOnScreen("assets\accountPasswordField.PNG")
signinBtn = pyautogui.locateCenterOnScreen("assets\signinBtn.PNG")
signinConfirmBtn = pyautogui.locateCenterOnScreen("assets\signinConfirmBtn.PNG")