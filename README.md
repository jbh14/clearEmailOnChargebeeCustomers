# clearEmailOnChargebeeCustomers
Created this simple script for clearing email on Chargebee Customers, which can't be done via bulk import or from SFDC managed package (no credentials/site provided here, use .env for those).  This could be easily updated/extended to make other updates/address other shortcomings of Chargebee's built-in import tool. 
Be sure you know what you're doing if using this, since it can delete data in your Chargebee site (production or test)!  

## Available Scripts
1. Running this locally, make the CB site name and API key available to the script by listing inside an `.env` file in your project directory as such:
```
CB_SITE_NAME = "<chargebee_site_name>"
API_KEY = "<api_key_created_from_within_Chargebee>" 
```
2. Create and activate a virtual environment:
```
python3 -m venv .venv       # Mac/Linux
python -m venv .venv        # Windows

source .venv/bin/activate   # Mac/Linux
.\venv\Scripts\activate     # Windows
```
3. Install required dependencies:
```
pip install -r requirements.txt
```
4. Run the script:
```
python3 clearCBcustomerEmails.py
```
