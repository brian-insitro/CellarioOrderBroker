import requests
import json

# Config
host = 'VM-AUTO-11.insitro.local'
#host = '172.16.14.205'
username = 'labadmin'
password = 'rebirth-logistic-smoke-BITUMEN'

def authenticate(host, username, password, timeout=10):
    url = f'http://{host}:8444/authenticate'
    
    payload = {
        'username': username,
        'password': password
    }

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        # Send the POST request for authentication with a timeout
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=timeout)
        
        if response.status_code == 200:
            print("Authentication successful!")
            print("Response:", response.json())
        else:
            print(f"Failed to authenticate. Status code: {response.status_code}")
            print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        print(f"An error occurred: {e}")

def check_system_status(host, timeout=10):
    url = f'http://{host}:8444/system'

    headers = {
        'Accept': 'application/json'
    }

    try:
        # Send the GET request with a timeout
        response = requests.get(url, headers=headers, timeout=timeout)
        
        
        # Handle the response
        if response.status_code == 200:
            print("System status fetched successfully!")
            print("Response:", response.json())
        else:
            print(f"Failed to fetch system status. Status code: {response.status_code}")
            print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        print(f"An error occurred: {e}")

def create_order(host, recipe, timeout=10):
    url = f'http://{host}:8444/orders'
    
    payload = {
        "recipe": recipe
    }

    headers = {
        'Content-Type': 'application/json'
    }
    
    try:
        # Send the POST request to create an order with a timeout
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=timeout)
        
        if response.status_code == 202:
            print("Order created successfully!")
            print("Response:", response.json())
        else:
            print(f"Failed to create order. Status code: {response.status_code}")
            print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        print(f"An error occurred: {e}")

recipe = {
  "Description": "This is a sample order description.",
  "User": "labadmin",
  "EmailRecipient": "brian@insitro.com",
  "InventoryScan": true,
  "ClearStorage": false,
  "ShouldBeValidated": true,
  "CreateDefaultParameters": true,
  "Template": {
    "TemplateId": 0,
    "BatchCount": 1
  }
}

create_order(host, recipe)
#check_system_status(host)
#authenticate(host, username, password)
