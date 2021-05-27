import os
import subprocess
import time as t
import sys

import config as conf
import additionalFunctions as af
import zoomFunctions as zf

zf.StartZoom()

# TODO: See if I can find a way later to auto check if logged in
# TODO: See if I can find a way later to auto check what account is logged in

# Check if already logged in
loginStatus = af.ConfirmLogin()

if loginStatus == "Yes":
    stayLoggedIn = af.stayLoggedInCheck()
    if stayLoggedIn == "Yes":
        print("You're logged into the account you need already. This app will now close.")
        sys.exit()
    elif stayLoggedIn == "No":
        # Logout of Zoom
        zf.signOut
        # Allow login to other account
        secretNamePrefix = af.selectAccount()
        zf.signIn(secretNamePrefix)
elif loginStatus == "No":
    secretNamePrefix = af.selectAccount()
    zf.signInButton()
    zf.signIn(secretNamePrefix)