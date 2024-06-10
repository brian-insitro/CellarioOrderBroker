import requests
import json

def send_to_cellario_services(mode, endpoint, payload):
    # Connection params
    host = 'VM-AUTO-11.insitro.local' #'172.16.14.205'
    port = '8444'
    timeout = 10
    
    url = f'http://{host}:{port}/{endpoint}'
    headers = { 'Content-Type': 'application/json' }
    
    try:
        if mode == 'POST':
            response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=timeout)
        elif mode == 'GET':
            response = requests.get(url, headers=headers, timeout=timeout)
        elif mode == 'PUT':
            response = requests.put(url, headers=headers, data=json.dumps(payload), timeout=timeout)
        elif mode == 'DELETE':
            response = requests.delete(url, headers=headers, timeout=timeout)
        else:
            print(f"Invalid mode: {mode}")
        
        if response.status_code == 202:
            print(f"{mode} request to {url} successful!")
            print("Response:", response.json())
        else:
            print(f"Failed to send {mode} request to {url}. Status code: {response.status_code}")
            print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
  
def send_post(endpoint, payload):
    send_to_cellario_services('POST', endpoint, payload)

def send_get(endpoint):
    send_to_cellario_services('GET', endpoint, None)

def send_put(endpoint, payload):
    send_to_cellario_services('PUT', endpoint, payload)

def send_delete(endpoint):
    send_to_cellario_services('DELETE', endpoint, None)


def create_order(order, payload):
    prefix = {
        "Description": '{order.OrderType}',
        "User": 'labadmin',
        "EmailRecipient": 'brian@insitro.com',
        "InventoryScan": True,
        "ClearStorage": False,
        "ShouldBeValidated": True
    }
    
    send_post('/orders', json.dumps({**prefix, **payload}))

template_recipe = {
    "Template": {
      "TemplateId": 1,
      "BatchCount": 1,
      "PlateSets": [
         {
            "PlateProtocolId": 0,
            "LabwareType": "",
            "PlacementProcess": "",
            "ExplicitCount": 0,
            "ResourcePositionId": 0,
            "OutputResourcePositionId": 0,
            "ExcludeThread": False,
            "Barcodes": [
               ""
            ]
         }
      ],
      "ScheduleDetail": {
         "ScheduleAt": "",
         "ProtocolStepId": 0,
         "ScheduledAfter": 0,
         "PlateNumber": 0
      }
   }
}

order_recipe = {
    "Order": {
      "ProtocolId": {order.protocol_id},
      "PlateSets": [
        {
          "PlateProtocolId": 0,
          "LabwareType": "",
          "PlacementProcess": "",
          "ExplicitCount": 0,
          "ResourcePositionId": 0,
          "OutputResourcePositionId": 0,
          "ExcludeThread": False,
          "Barcodes": [
            ""
          ]
        }
      ],
      "ScheduleDetail": {
        "ScheduleAt": "",
        "ProtocolStepId": 0,
        "ScheduledAfter": 0,
        "PlateNumber": 0
      }
    }
}

#create_order(host, order_recipe)
#check_system_status(host)
#authenticate(host, username, password)

