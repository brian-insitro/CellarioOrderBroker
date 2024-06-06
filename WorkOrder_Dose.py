from WorkOrder import WorkOrder

class WorkOrder_Dose(WorkOrder):
    order_type = "Dose"
    schema = {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "OrderType": {
          "type": "string",
          "description": "Type of order"
        },
        "OrderID": {
          "type": "string",
          "description": "Identifier for the order"
        },
        "Transfers": {
          "type": "array",
          "description": "Array of transfers",
          "items": {
            "type": "object",
            "properties": {
              "SourceBarcode": {
                "type": "string",
                "description": "Source plate barcode"
              },
              "SourceWell": {
                "type": "string",
                "description": "Source plate barcode"
              },
              "DestBarcode": {
                "type": "string",
                "description": "Destination plate barcode"
              },
              "DestWell": {
                "type": "string",
                "description": "Destination well identifier"
              },
              "Volume": {
                "type": "number",
                "description": "Volume in microliters (µL)"
              },
              "Comment": {
                "type": "string",
                "description": "Optional comment"
              }
            },
            "required": [
              "SourceBarcode",
              "SourceWell",
              "DestBarcode",
              "DestWell",
              "Volume",
              "Comment"
            ]
          }
        },
        "Comment": {
          "type": "string",
          "description": "Optional comment"
        }
      },
      "required": [
        "OrderType",
        "OrderID",
        "Transfers",
        "Comment"
      ]
    }

    @classmethod
    def process(cls, data):
        print("Processing Dose Work Order")
        # Add processing logic here
