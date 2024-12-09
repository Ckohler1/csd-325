#Colton Kohler
#12/8/2024
#module 9.2 test
import requests
import json

def jprint(obj):
    # Convert the Python object to a formatted JSON string
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Make the request
response = requests.get("http://api.open-notify.org/astros/")

# Output the connection test result
print("Connection test result:")
print(f"Status Code: {response.status_code}")
print(f"Connection successful: {response.status_code == 200}")

# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON and print it using jprint
    data = response.json()
    jprint(data)
else:
    print(f"Error: {response.status_code}")
