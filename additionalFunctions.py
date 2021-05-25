import os
import pandas as pd
import json

#Check if user logged in

#Select Login Account from List
def selectAccount():
    secretName = ""
    accountList = []
    
    print("Started reading JSON file containing account list")
    with open('accounts.json') as f:
        for jsonObj in f:
            accountDict = json.loads(jsonObj)
            accountList.append(accountDict)

    print("Printing each JSON Decoded Object")
    for account in accountList:
        print(account["id"] + " - " + account["AccountNickname"] + " - " + account["AccountEmail"])
    
    choice = raw_input("Type the Number that corresponds with the account you wish to login with and press enter:")

    listItem = choice - 1

    secretName = account[listItem].SecretName

    return secretName