import pyautogui

#Program File Locations
startfile = "C:/Program Files (x86)/Zoom/bin/Zoom.exe"

#Button Image Assets
signinEmailfield = pyautogui.locateCenterOnScreen("accountEmailField.PNG")
signinPasswordfield = pyautogui.locateCenterOnScreen("accountPasswordField.PNG")
signinBtn = pyautogui.locateCenterOnScreen("signinBtn.PNG")
signinConfirmBtn = pyautogui.locateCenterOnScreen("signinConfirmBtn.PNG")
loginStatusIcon = pyautogui.locateCenterOnScreen("loginStatusIcon.PNG")
signOutBtn = pyautogui.locateCenterOnScreen("signOutBtn.PNG")