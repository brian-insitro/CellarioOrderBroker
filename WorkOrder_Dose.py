from WorkOrder import WorkOrder
import csv

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
        
        csv_filename = 'toEcho.csv'
        csv_headers = ['Source Plate Name', 'Source Well', 'Destination Plate Name', 'Destination Well', 'Transfer Volume', 'Comment']
        json_headers = cls.schema["properties"]["Transfers"]["items"]["properties"].keys()

        # Convert to csv
        with open(csv_filename, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
            writer.writeheader()
            for transfer in data["Transfers"]:
              writer.writerow({csv_header: transfer[json_header] for csv_header, json_header in zip(csv_headers, json_headers)})
    