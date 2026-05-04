# Point of Sale System

This is a basic Point of Sale (POS) System with Google Sheets Integration.

## Features:
- Manage inventory
- Process sales
- Generate sales reports

## Google Sheets Integration:
The integration allows you to log sales data directly into a Google Sheets document. This can be set up using the Google Sheets API.

# Starter Code

```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Setup the Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/credentials.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheet
document = client.open("POS Data")
worksheet = document.sheet1

# Function to log a sale

def log_sale(item, quantity, price):
    total = quantity * price
    worksheet.append_row([item, quantity, price, total])
    print(f'Sale logged: {item}, Quantity: {quantity}, Total: {total}')
```

```python
# Inventory Management

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity, price):
        self.items[item_name] = {'quantity': quantity, 'price': price}

    def sell_item(self, item_name, quantity):
        if item_name in self.items and self.items[item_name]['quantity'] >= quantity:
            self.items[item_name]['quantity'] -= quantity
            log_sale(item_name, quantity, self.items[item_name]['price'])
            print(f'Sold {quantity} of {item_name}')
        else:
            print('Item not available or insufficient quantity.')

# Sample usage:
inventory = Inventory()
inventory.add_item('Coffee', 10, 2.5)
inventory.sell_item('Coffee', 2)
```