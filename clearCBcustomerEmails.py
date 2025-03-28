import os
import requests
import base64
from dotenv import load_dotenv
from readCustomerIDs import read_customer_ids

# Load environment variables from .env file
load_dotenv()

# get API credentials from env variables
if not os.getenv("CB_SITE_NAME"):
    raise ValueError("CB_SITE_NAME is not set in the environment variables")
if not os.getenv("API_KEY"):
    raise ValueError("API_KEY is not set in the environment variables")
BASE_URL = "https://" + os.getenv("CB_SITE_NAME") + ".chargebee.com/api/v2/customers/"
API_KEY = os.getenv("API_KEY")

# Encode API Key in Base64
AUTH_HEADER = base64.b64encode(f"{API_KEY}:".encode()).decode()
HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Basic {AUTH_HEADER}"
}

# Load customer IDs from CSV
customer_ids = read_customer_ids("customers.csv", "customer_id") # 1st parameter is the CSV filename, 2nd parameter is the column header for customer IDs

def update_customer(customer_id):
    url = f"{BASE_URL}{customer_id}"
    response = requests.post(url, headers=HEADERS, data={"email": ""})
    if response.status_code == 200:
        print(f"Success: {response.json()}")
    else:
        print(f"Error ({response.status_code}): {response.text}")

# Loop through each customer ID and send request
for customer_id in customer_ids:
    update_customer(customer_id)