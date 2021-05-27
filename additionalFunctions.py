import json
import sys

###########################################
# Check if user logged in
###########################################
def ConfirmLogin():
    loginStatus = ""

    while True:
        # Ask if user is logged in
        print("Are you currently logged in?")
        print("1: Yes")
        print("2: No")
        print("3: Exit Program")
        choice = input("Type the number that corresponds with whether you are logged in or not, or type 3 to exit. Then press the Enter key to continue.")
        
        switcher = {
            "1": "Yes",
            "2": "No",
            "3": "Exit"
        }
        
        try:
            val = int(choice) # Just checks to make sure the user entered a number

            if choice == "3":
                sys.exit()
            elif choice == "2":
                break
        except ValueError:
                print("You entered something other than a number. Please try again.")

    loginStatus == switcher.get(choice, "Invalid number entered.")
    return loginStatus

###########################################
# Verify User wishes to remain logged in
###########################################
def stayLoggedInCheck():
    stayLoggedIn = ""

    while True:
        # Ask if user is logged in
        print("Do you wish to remain logged in to the current account?")
        print("1: Yes")
        print("2: No")
        print("3: Exit Program")
        choice = input("Type the number that corresponds with whether you are logged in or not, or type 3 to exit. Then press the Enter key to continue.")

        switcher = {
            "1": "Yes",
            "2": "No",
            "3": "Exit"
        }

        try:
            val = int(choice) # Just checks to make sure the user entered a number

            if choice == "1":
                print("Logged into account you need already. This app will now close.")
                sys.exit()
            elif choice == "3":
                sys.exit()
            else:
                break
        except ValueError:
                print("You entered something other than a number. Please try again.")

    stayLoggedIn == switcher.get(choice, "Invalid number entered.")
    return stayLoggedIn

###########################################
# Select Login Account from List
###########################################
def selectAccount():
    accountList = []
    secretNamePrefix = ""
    
    print("Started reading account list")
    
    with open('accounts.json') as f:
        for jsonObj in f:
            accountDict = json.loads(jsonObj)
            accountList.append(accountDict)

    print("Printing list of accounts to pick from:")
    for account in accountList:
        print(account["id"] + " - " + account["AccountNickname"] + " - " + account["AccountEmail"])


    while True:
        choice = input("Type the Number that corresponds with the account you wish to login with and press enter:")

        try:
            val = int(choice) # Just checks to make sure the user entered a number
            
            # Checks if choice is actually in the account list
            if val in accountList.values():
                for account in accountList:
                    if choice == account["id"]:
                        break
                    elif choice != account["id"]:
                        continue
            else:
                print('Your choice was not in the list. Please try again.')
                continue
        except ValueError:
            print("You entered something other than a number. Please try again.")
            continue
    
    secretNamePrefix = account["SecretName"]
    return secretNamePrefix