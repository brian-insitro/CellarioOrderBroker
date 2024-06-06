class WorkOrderFactory:
    registry = {}

    @classmethod
    def register(cls, work_order_cls):
        cls.registry[work_order_cls.order_type] = work_order_cls

    @classmethod
    def create(cls, order_type, data):
        work_order_cls = cls.registry.get(order_type)
        if not work_order_cls:
            raise ValueError(f"Unsupported OrderType: {order_type}")
        work_order_cls.validate(data)
        return work_order_cls
