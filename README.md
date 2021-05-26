# Zoom-Account-Switch
Application allowing the user to easily switch between Zoom accounts.

## Pre-requisites

- This script was written to work in Windows 10
  - It may be possible to get it to work on other OSs, but it will most likely require some reworking of the script.
- You will need a Key Vault in Azure and will need to login to your Azure instance in Powershell to use this.
  - You DO NOT have to login to Azure before running the script every time. Your system should maintain a connection for a time. However, if you run into issues, you may need to re-run the `az login` command to refresh your connection.

## Required Python Modules

Make sure you have Python installed. I created this using Python 3.9.5 and pip version 21.1.2, but older versions may still work. The following additional Python modules need to be installed.

- pandas
- pyautogui
- pillow
- azure-identity
- azure-keyvault-secrets

### Installing Python Modules

Module installation can be accomplished using the following command:

`python -m pip install <modulename>`

This does require that you have *pip* installed as well. For details on how to install pip, check out the official [pip documentation Installation page](https://pip.pypa.io/en/stable/installing/).

## Required Powershell Modules

Because this script uses Azure Key Vault to grab your Zoom Credentials, you will need to have the `az` Powershell module installed to login to Azure via the command line.

From there you can:

1. Open a Powershell window.
2. Type the command `az login`
3. Login to your Azure instance where your Key Vault containing your Zoom credentials is located.

### Alternate Method

Alternatively, you can use the Powershell script named `AzureLogin.ps1`. It will install the needed modules and start the login process.

### Installing Powershell Modules

Install Powershell modules with the following command:

`Install-Module -Name <ModuleName> -Scope CurrentUser -Repository PSGallery -Force`

### Set Execution Policy

Make sure you can run powershell scripts (it is disabled by default). Additional information on this can be found at: (http://technet.microsoft.com/en-us/library/ee176949.aspx)[http://technet.microsoft.com/en-us/library/ee176949.aspx]. Use the following command to set the policy appropriately.

`Set-ExecutionPolicy RemoteSigned`

## Azure KeyVault

You will need to have your Zoom passwords stored in an Azure KeyVault for this to work. This is to help limit when your passwords are exposed at all.
You will also need to login to your Azure instance in command line.

## Resources

This section lists resources I referenced while working on this project.

### Zoom Pages

These pages are from official Zoom sources and/or forums.

- [Zoom Developer](https://developers.zoom.us/)
- [Zoom Developer Forum - Login from the command line](https://devforum.zoom.us/t/log-in-from-command-line/7804)

### Microsoft Pages

These pages are official Microsoft documentation.

- [Microsoft Docs - Quickstart: Azure Key Vault secret client library for Python](https://docs.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python)

### Python Pages

These pages come from the Python Software Foundation site.

- [Python Software Foundation - azure-keyvault-secrets](https://pypi.org/project/azure-keyvault-secrets/)

### W3Schools Pages

These pages are from W3Schools.

- [W3Schools - Python User Input](https://www.w3schools.com/python/python_user_input.asp)

### Stack Overflow Pages

These pages are from Stack Overflow.

- [Python: restarting a loop](https://stackoverflow.com/questions/492860/python-restarting-a-loop)
- [Python: Return hash values from hash table regarding to a searching keyword](https://stackoverflow.com/questions/20072014/python-return-hash-values-from-hash-table-regarding-to-a-searching-keyword)
- [How to check if string input is a number?](https://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number)
- [Pillow package is required but i already have the latest version](https://stackoverflow.com/questions/65318814/pillow-package-is-required-but-i-already-have-the-latest-version)

### Youtube Videos

- [Accessing Azure Key Vault with Python](https://www.youtube.com/watch?v=FI44MhwklSc)

### Miscellaeous Sources

- [Medium - Automating Zoom with Python](https://medium.com/asecuritysite-when-bob-met-alice/automating-zoom-with-python-b333ff81c69f)
- [Dev.to - Automating Zoom](https://dev.to/sunilaleti/automating-zoom-3e64)
- [Check if the dictionary key / value exists in Python](https://note.nkmk.me/en/python-dict-in-values-items/#:~:text=In%20Python%2C%20use%20the%20in,is%20a%20member%20of%20dict%20).&text=The%20values()%20and%20items,dictionary%20in%20a%20for%20loop.)
- [Python add to Dictionary](https://www.journaldev.com/23232/python-add-to-dictionary#:~:text=There%20is%20no%20explicitly%20defined,assignment%20operator%20with%20dictionary%20key.&text=Note%20that%20if%20the%20key,the%20value%20will%20be%20overwritten.)
- [Tutorials Point - Python - Hash Table](https://www.tutorialspoint.com/python_data_structure/python_hash_table.htm)
- [PYnative - Python Parse multiple JSON objects from file](https://pynative.com/python-parse-multiple-json-objects-from-file/)