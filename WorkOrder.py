import jsonschema

class WorkOrder:
    order_type = None
    schema = None

    @classmethod
    def validate(cls, data):
        jsonschema.validate(instance=data, schema=cls.schema)

    @classmethod
    def process(cls, data):
        raise NotImplementedError("Subclasses must implement this method")

