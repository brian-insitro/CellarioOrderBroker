from WorkOrder import WorkOrder

class WorkOrder_Image(WorkOrder):
    order_type = "Image"
    protocol_id = 2
    schema = {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "PlateBarcode": {
          "type": "string",
          "description": "Plate barcode"
        },
        "ImagingMode": {
          "type": "string",
          "enum": ["DPC", "Absorbance-AlluraRed_5X", "Fluorescent-DAPI"],
          "description": "Imaging modality"
        },
        "Wells": {
          "type": "array",
          "description": "Array of wells to image",
          "items": {
            "type": "object",
            "properties": {
              "WellNumber": {
                "type": "string",
                "description": "Source plate barcode"
              }
            },
            "required": [
              "WellNumber"
            ]
          }
        }
      },
      "required": [
        "PlateBarcode",
        "ImagingMode",
        "Wells"
      ]
    }

    @classmethod
    def process(cls, data):
        print("Processing Image Work Order")
        # Add processing logic here
