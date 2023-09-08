import subprocess
import requests
#
# # Get the host name from PowerShell
# result = subprocess.run(["powershell", "Get-Host"], capture_output=True, text=True)
# output = result.stdout
# print(output)

# Set the host and port variables
HOST = "127.0.0.2" # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

# Make a GET request to the running server
response = requests.get(f"http://{HOST}:{PORT}")
# Print the status code and the content of the response
print(response.status_code)
print(response.text)
