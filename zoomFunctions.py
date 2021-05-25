import os
import pyautogui
import time as t

import settings as s
import keyvault as kv
import additionalFunctions as af

# Confirm if user already logged in
# def confirmLogin():

# The signOnButton function is for if you have to sign in
# without logging out of another account first.
def signInButton():
    # Click the Sign In button
    pyautogui.moveTo(s.signinBtn)
    pyautogui.click()
    t.sleep(1)

def signIn(AccountInfo):
    print(AccountInfo)

    # secretName = AccountInfo["SecretName"].Value
    # accountEmail = AccountInfo["AccountEmail"].Value
    secretName = AccountInfo.SecretName
    accountEmail = AccountInfo.AccountEmail

    print(secretName)
    print(accountEmail)

    # Retrieve password for selected account
    accountPassword = kv.retrieveSecret(secretName)

    #Enter's Email Address for Account
    pyautogui.moveTo(s.signinEmailfield)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    # Clear field if it already has anything in it
    pyautogui.write(accountEmail)
    t.sleep(1)

    # Enter's Password for Account
    pyautogui.moveTo(s.signinPasswordfield)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.write(accountPassword)
    t.sleep(1)

    # Click's the sign in confirmation button
    pyautogui.moveTo(s.signinConfirmBtn)
    pyautogui.click()
    t.sleep(1)

# Handles logging out of the Zoom Account
def signOut():
    pyautogui.moveTo(s.loginStatusIcon)
    pyautogui.click()
    t.sleep(1)
    pyautogui.moveTo(s.signOutBtn)
    pyautogui.click()
    t.sleep(1)