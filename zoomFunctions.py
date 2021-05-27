import os
import pyautogui
import time as t

import config as conf
import keyvault as kv
import additionalFunctions as af

def StartZoom():
    os.startfile(conf.startfile)
    t.sleep(3)

# Confirm if user already logged in
# def confirmLogin():

# The signOnButton function is for if you have to sign in
# without logging out of another account first.
def signInButton():
    # Click the Sign In button
    pyautogui.moveTo(conf.signinBtn)
    pyautogui.click()
    t.sleep(1)

def signIn(SecretNamePrefix):
    print ("Starting the signin process, please give us a moment.")

    emailSecretName = SecretNamePrefix + "_Email"
    passwordSecretName = SecretNamePrefix + "_Password"
    
    # Retrieve email and password for selected account
    accountEmail = kv.retrieveSecret(emailSecretName)
    accountPassword = kv.retrieveSecret(passwordSecretName)

    #Enter's Email Address for Account
    pyautogui.moveTo(conf.signinEmailfield)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    # Clear field if it already has anything in it
    pyautogui.write(accountEmail)
    t.sleep(1)

    # Enter's Password for Account
    pyautogui.moveTo(conf.signinPasswordfield)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.write(accountPassword)
    t.sleep(1)

    # Click's the sign in confirmation button
    pyautogui.moveTo(conf.signinConfirmBtn)
    pyautogui.click()
    t.sleep(1)

    print ("Successfully signed in.")

# Handles logging out of the Zoom Account
def signOut():
    print ("Signing you out of the unwanted account. Please give me a moment.")

    pyautogui.moveTo(conf.loginStatusIcon)
    pyautogui.click()
    t.sleep(1)

    pyautogui.moveTo(conf.signOutBtn)
    pyautogui.click()
    t.sleep(1)

    print ("Signed out, starting process to log you into another account.")