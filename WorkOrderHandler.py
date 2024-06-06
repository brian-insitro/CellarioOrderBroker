import json
import jsonschema
from WorkOrderFactory import WorkOrderFactory

def route_order(input_json):
    try:
        order = json.loads(input_json)
        order_type = order.get('OrderType')
        
        if not order_type:
            raise ValueError("OrderType is missing from the input JSON")
        
        # Create appropriate work order class, validate input, then process
        work_order_cls = WorkOrderFactory.create(order_type, order)
        work_order_cls.validate(order)
        work_order_cls.process(order)
    
    except json.JSONDecodeError:
        print("Invalid JSON input")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except jsonschema.exceptions.ValidationError as ve:
        print(f"JSON Schema validation error: {ve.message}")


# Import and register each work order to be handled
from WorkOrder_Dose import WorkOrder_Dose
WorkOrderFactory.register(WorkOrder_Dose)

from WorkOrder_Feed import WorkOrder_Feed
WorkOrderFactory.register(WorkOrder_Feed)

from WorkOrder_Image import WorkOrder_Image
WorkOrderFactory.register(WorkOrder_Image)
