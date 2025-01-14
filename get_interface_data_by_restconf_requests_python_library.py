import requests
import json
from urllib3.exceptions import InsecureRequestWarning

# Disable SSL warnings for self-signed certificates
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Router configuration
router_ip = "192.168.96.133"
username = "admin"
password = "Hellog@123"

# RESTCONF API URL for GigabitEthernet interfaces
url = f"https://{router_ip}:443/restconf/data/Cisco-IOS-XE-native:native/interface"

# HTTP Headers
headers = {
    'Accept': 'application/yang-data+json',
    'Authorization': f"Basic YWRtaW46SGVsbG9nQDEyMw=="  # Base64 of "admin:Hellog@123"
}

try:
    # Send GET request to the router
    print(f"Sending GET request to {url}")
    response = requests.get(url, headers=headers, verify=False)

    # Check the HTTP response code
    if response.status_code == 200:
        print("\nSuccessfully fetched data from the router!")
        
        # Print the raw JSON response for inspection
        print("\nRaw JSON Response:")
        print(json.dumps(response.json(), indent=2))

    else:
        print(f"\nFailed to fetch data. HTTP Status Code: {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
