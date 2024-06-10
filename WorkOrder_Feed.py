from WorkOrder import WorkOrder

class WorkOrder_Feed(WorkOrder):
    order_type = "Feed"
    protocol_id = 1
    schema = {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
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
