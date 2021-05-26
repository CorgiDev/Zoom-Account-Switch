Set-ExecutionPolicy RemoteSigned # Requires run as administrator

# If unable to run as Admin, comment out the other Set-Execution Policy Line
# and use the one below to set policy as needed.
# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

Write-Output y | Install-Module -Name PackageManagement -Force -MinimumVersion 1.4.6 -Scope CurrentUser -AllowClobber -Repository PSGallery

Write-Output y | Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force

$PSVersionTable.PSVersion

az login

# Connect-AzAccount