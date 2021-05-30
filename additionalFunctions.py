import json
import sys

###########################################
# Check if user logged in
###########################################
def ConfirmLogin():
    loginStatus = ""
    
    while True:
        # TODO: Find a way to automate checking if user is logged in or not.
        # Ask if user is logged in
        print("Are you currently logged in?")
        print("1: Yes")
        print("2: No")
        print("3: Exit Program")
        response = input("Type the number that corresponds with whether you are logged in or not, or type 3 to exit. Then press the Enter key to continue.")
        
        try:
            val = int(response) # Just checks to make sure the user entered a number

            if response == "3":
                print("You don't need me then. I am going back to bed. Bye.")
                sys.exit()
            elif response == "2":
                loginStatus = "No"
                break
            elif response == "1":
                loginStatus = "Yes"
                break
            else:
                print("You entered an invalid number. Please try again.")
                continue
        except ValueError:
                print("You entered something other than a number. Please try again.")

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
        response = input("Type the number that corresponds with whether you are logged in or not, or type 3 to exit. Then press the Enter key to continue.")

        try:
            val = int(response) # Just checks to make sure the user entered a number

            if response == "3":
                print("You don't need me then. I am going back to bed. Bye.")
                sys.exit()
            elif response == "2":
                stayLoggedIn = "No"
                break
            elif response == "1":
                stayLoggedIn = "Yes"
                break
        except ValueError:
                print("You entered something other than a number. Please try again.")

    return stayLoggedIn

###########################################
# Select Login Account from List
###########################################
def selectAccount():
    accountList = []
    secretNamePrefix = ""
    response = ""
    
    print("Started reading account list")
    
    with open('accounts.json') as f:
        for jsonObj in f:
            accountDict = json.loads(jsonObj)
            accountList.append(accountDict)

    print("Printing list of accounts to pick from:")
    for account in accountList:
        print(account["id"] + " - " + account["AccountNickname"] + " - " + account["AccountEmail"])


    while True:
        response = input("Type the Number that corresponds with the account you wish to login with and press enter:")

        try:
            val = int(response) # Just checks to make sure the user entered a number
            
            # Checks if response is actually in the account list
            if val in accountList.values():
                for account in accountList:
                    if response == account["id"]:
                        secretNamePrefix = account["SecretName"]
                        break
                    elif response != account["id"]:
                        continue
            else:
                print('Your response was not in the list. Please try again.')
                continue
        except ValueError:
            print("You entered something other than a number. Please try again.")
            continue
    
    return secretNamePrefix