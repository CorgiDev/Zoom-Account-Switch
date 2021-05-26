# If unable to run as Admin, comment out the 4 lines of commands under
# "Requires run as administrator", and use the ones below. 
# These second set of commands set scope to current user, 
# which generally does not require the use of Admin privileges.

# Requires run as administrator
Set-ExecutionPolicy RemoteSigned
Echo y | Install-Module -Name PowerShellGet -Force
Echo y | Install-Module -Name PackageManagement -Force -MinimumVersion 1.4.6 -AllowClobber -Repository PSGallery
Echo y | Install-Module -Name Az -Repository PSGallery -Force

# Do not require run as administrator
# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
# Echo y | Install-Module -Name PowerShellGet -Scope CurrentUser -Force
# Echo y | Install-Module -Name PackageManagement -Scope CurrentUser -Force -MinimumVersion 1.4.6 -Scope CurrentUser -AllowClobber -Repository PSGallery
# Echo y | Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force

$PSVersionTable.PSVersion

# Log in to your Azure subscription
Write-Output("An Azure Login browser window will open. Make sure to login with the Azure account where your Zoom credentials are present.")

Start-Sleep -s 5

az login