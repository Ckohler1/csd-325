#Colton Kohler
#12/8/2024
#module 9.2 assignment
import requests
import json

# Function to print JSON with formatting
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# API endpoint
url = "https://anapioficeandfire.com/api/houses/378"

# Test the connection to the API
response = requests.get(url)

# Output the connection test results
print("Connection test result:")
print(f"Status Code: {response.status_code}")
print(f"Connection successful: {response.status_code == 200}")

# Output results (raw response)
print("\nRaw response:")
print(response.text)

# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON and print it using jprint
    data = response.json()
    print("\nFormatted response:")
    jprint(data)
else:
    print(f"Error: {response.status_code}")
