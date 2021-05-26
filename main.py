import os
import subprocess
import time as t
import sys

import settings as s
import additionalFunctions as af
import zoomFunctions as zf

# Login to your Azure subscription where Key Vault is located
subprocess.Popen(['powershell.exe', 'AzureLogin.ps1'], stdout=sys.stdout)

# Open Zoom
os.startfile(s.startfile)
t.sleep(3)

# TODO: See if I can find a way later to auto check if logged in
# TODO: See if I can find a way later to auto check what account is logged in

# Check if already logged in
loginStatus = af.ConfirmLogin

if loginStatus == "Yes":
    stayLoggedIn = af.stayLoggedInCheck
    if stayLoggedIn == "Yes":
        print ("Logged into account you need already. This app will now close.")
        sys.exit ()
    elif stayLoggedIn == "No":
        # Logout of Zoom
        zf.signOut
        # Allow login to other account
        accountInfo = af.selectAccount
        zf.signIn (accountInfo)
elif loginStatus == "No":
    accountInfo = af.selectAccount
    zf.signInButton ()
    zf.signIn (accountInfo)