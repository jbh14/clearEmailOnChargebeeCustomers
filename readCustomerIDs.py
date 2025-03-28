import csv

# Function to read customer IDs from CSV 
def read_customer_ids(csv_filename, customer_id_col_header="customer_id") -> list:
    customer_ids = []
    with open(csv_filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # Reads CSV into a dictionary format
        for row in reader:
            customer_ids.append(row[customer_id_col_header])  # Assumes first column is "customer_id"
    return customer_ids