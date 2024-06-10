import jsonschema

# Base class for all work orders
class WorkOrder:
    order_type = None
    protocol_id = None
    schema = None
    
    @classmethod
    def validate_base(cls, data):
        base_schema = {
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
                "Comment": {
                  "type": "string",
                  "description": "Optional comment"
                }
            },
            "required": [
                "OrderType",
                "OrderID",
                "Comment"
            ]
        }
        jsonschema.validate(instance=data, schema=base_schema)

    @classmethod
    def validate(cls, data):
        cls.validate_base(data)
        jsonschema.validate(instance=data, schema=cls.schema)

    @classmethod
    def process(cls, data):
        raise NotImplementedError("Subclasses must implement this method")

