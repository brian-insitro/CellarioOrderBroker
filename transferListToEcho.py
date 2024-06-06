import csv

def convert_to_csv(data, csv_filename):
    """
    Converts data dictionary matching the specified schema into a CSV file.

    Parameters:
    - data (dict): The data dictionary matching the schema
    - csv_filename (str): The name of the output CSV file
    """
    
    headers = ['Source Plate Name', 'Source Well', 'Destination Plate Name', 'Destination Well', 'Transfer Volume', 'Comment']

    if "Transfers" not in data:
        raise ValueError("The provided data does not contain the 'Transfers' key")
    transfers = data["Transfers"]

    # Open the CSV file for writing
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        
        # Write the header
        writer.writeheader()
        
        # Write the rows
        for transfer in transfers:
            if all(key in transfer for key in headers):
                writer.writerow({
                    headers[0]: transfer['SourceBarcode'],
                    headers[1]: transfer['SourceWell'],
                    headers[2]: transfer['DestBarcode'],
                    headers[3]: transfer['DestWell'],
                    headers[4]: transfer['Volume'],
                    headers[5]: transfer['Comment']
                })
            else:
                raise ValueError(f"One of the transfers is missing required keys: {transfer}")

# Example usage
data_example = {
    "OrderType": "Feed",
    "OrderID": "12345",
    "Transfers": [
        {
            "SourceBarcode": "SB001",
            "SourceWell": "A1",
            "DestBarcode": "DB001",
            "DestWell": "B1",
            "Volume": 50.0
        },
        {
            "SourceBarcode": "SB002",
            "SourceWell": "A2",
            "DestBarcode": "DB002",
            "DestWell": "B2",
            "Volume": 75.0
        }
    ]
}

convert_to_csv(data_example, 'output.csv')
