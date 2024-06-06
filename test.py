import WorkOrderHandler

input_json_feed = '''
{
    "OrderType": "Feed",
    "OrderID": "1001",
    "PlateBarcode": "ABC123",
    "MediaType": "TypeA",
    "VolumeRemaining": 50.0,
    "VolumeAdded": 10.0
}
'''

input_json_image = '''
{
    "OrderType": "Image",
    "OrderID": "1002",
    "PlateBarcode": "123-OP",
    "ImagingMode": "DPC",
    "Wells": [
        {
          "WellNumber": "A1"
        },
        {
          "WellNumber": "B2"
        },
        {
          "WellNumber": "C3"
        },
        {
          "WellNumber": "D4"
        },
        {
          "WellNumber": "E5"
        }
    ]
}
'''

input_json_dose = '''
{
    "OrderType": "Dose",
    "OrderID": "1003",
    "Transfers": [
        {
            "SourceBarcode": "SB003",
            "SourceWell": "A3",
            "DestBarcode": "DB003",
            "DestWell": "A6",
            "Volume": 20.0,
            "Comment": "dose"
        },
        {
            "SourceBarcode": "SB003",
            "SourceWell": "A5",
            "DestBarcode": "DB003",
            "DestWell": "B7",
            "Volume": 21.0,
            "Comment": "dose"
        },
        {
            "SourceBarcode": "SB004",
            "SourceWell": "B3",
            "DestBarcode": "DB003",
            "DestWell": "A6",
            "Volume": 22.0,
            "Comment": "backfill"
        },
        {
            "SourceBarcode": "SB004",
            "SourceWell": "B5",
            "DestBarcode": "DB003",
            "DestWell": "B7",
            "Volume": 23.0,
            "Comment": "backfill"
        }
    ],
    "Comment": "Dose order comment"
}
'''

WorkOrderHandler.route_order(input_json_feed)
WorkOrderHandler.route_order(input_json_image)
WorkOrderHandler.route_order(input_json_dose)
