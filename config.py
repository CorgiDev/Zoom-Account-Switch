import pyautogui
from os import environ as env

#Program File Locations
startfile = 'C:/Program Files (x86)/Zoom/bin/Zoom.exe'

#Button Image Assets
signinEmailfield = pyautogui.locateCenterOnScreen('./assets/accountEmailField.PNG')
signinPasswordfield = pyautogui.locateCenterOnScreen('./assets/accountPasswordField.PNG')
signinBtn = pyautogui.locateCenterOnScreen('./assets/signinBtn.PNG')
signinConfirmBtn = pyautogui.locateCenterOnScreen('./assets/signinConfirmBtn.PNG')
loginStatusIcon = pyautogui.locateCenterOnScreen('./assets/loginStatusIcon.PNG')
signOutBtn = pyautogui.locateCenterOnScreen('./assets/signOutBtn.PNG')

# Azure Variables
CLIENT_ID = env.get("AZURE_CLIENT_ID","")
CLIENT_SECRET = env.get("AZURE_CLIENT_SECRET","")
TENANT_ID = env.get("AZURE_TENANT_ID","")
KEYVAULT_NAME = env.get("AZURE_KEYVAULT_NAME","")
KEYVAULT_URI = f"https://{KEYVAULT_NAME}.vault.azure.net"