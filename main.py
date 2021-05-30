import sys

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
        print("You don't need me then. I am going back to bed. Bye.")
        sys.exit()
        # TODO: Maybe add a part here to let the user join a meeting if they want.
    elif stayLoggedIn == "No":
        zf.signOut()
        # Allow login to other account
        secretNamePrefix = af.selectAccount()
        zf.signIn(secretNamePrefix)
        # TODO: Maybe add a part here to let the user join a meeting if they want.
elif loginStatus == "No":
    secretNamePrefix = af.selectAccount()
    zf.signInButton()
    zf.signIn(secretNamePrefix)
    # TODO: Maybe add a part here to let the user join a meeting if they want.