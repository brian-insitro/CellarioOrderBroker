from WorkOrder import WorkOrder

class WorkOrder_Feed(WorkOrder):
    order_type = "Feed"
    schema = {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "OrderType": {
          "type": "string",
          "enum": ["Feed"],
          "description": "The type of the order, which is Feed"
        },
        "OrderID": {
          "type": "string",
          "description": "Identifier for the order"
        },
        "PlateBarcode": {
          "type": "string",
          "description": "Barcode of the plate"
        },
        "MediaType": {
          "type": "string",
          "description": "Type of media"
        },
        "VolumeRemaining": {
          "type": "number",
          "description": "Volume remaining in the plate after aspiration"
        },
        "VolumeAdded": {
          "type": "number",
          "description": "Volume added to the plate"
        }
      },
      "required": [
        "OrderType",
        "OrderID",
        "PlateBarcode",
        "MediaType",
        "VolumeRemaining",
        "VolumeAdded"
      ]
    }

    @classmethod
    def process(cls, data):
        print("Processing Feed Work Order")
        # Add processing logic here
