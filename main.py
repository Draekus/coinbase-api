"""Main.py"""
from dotenv import dotenv_values
import requests
from coinbase_api.coinbase import CoinbaseWalletAuth


# Load environment variables from .env
config = dotenv_values(".env")

# Set API key and secret
API_KEY = config["API_KEY"]
API_SECRET = config["API_SECRET"]
API_VERSION = config["API_VERSION"]


### Test Classes For Data Extraction ###
class User:
    """User class for storing user data."""

    def __init__(self, id, name, native_currency, resource_path) -> None:
        self.id = id
        self.name = name
        self.native_currency = native_currency
        self.resource_path = resource_path
        self.accounts = []

    def add_account(self, new_account):
        """Add account to user."""
        self.accounts.append(new_account)

    def __str__(self) -> str:
        return (
            f"User ID: {self.id}\nName: {self.name}\nNative Currency: "
            + f"{self.native_currency}\nResource Path: {self.resource_path}\n"
        )


# Set API URL
api_url = "https://api.coinbase.com/v2/"
# Generate auth headers
auth = CoinbaseWalletAuth(API_KEY, API_SECRET, API_VERSION)

# Get current user
r = requests.get(api_url + "user", auth=auth, timeout=5)
# Verify ssl certificate of request matches coinbase

r.raise_for_status()

# Print status code
print(r.status_code)
# Create user object
user = User(
    r.json()["data"]["id"],
    r.json()["data"]["name"],
    r.json()["data"]["native_currency"],
    r.json()["data"]["resource_path"],
)
# Print user data to console
print(user)

# Get user accounts
api_url = "https://api.coinbase.com/v2/accounts/"
r = requests.get(api_url, auth=auth, timeout=5)
print(r.status_code)

# For each account pretty print the name, balance, currency, and resource path
for account in r.json()["data"]:
    # Add account to user
    user.add_account(account)
    print(
        f"Account Name: {account['name']}\nBalance: {account['balance']['amount']}"
        + f" {account['balance']['currency']}\nResource Path: {account['resource_path']}\n"
    )

# Get account transactions
api_url = "https://api.coinbase.com/v2/accounts/f05c4c43-7d36-53b4-b913-fba2fd01d096/transactions"
r = requests.get(api_url, auth=auth, timeout=5)
print(r.status_code)
print(r.json())
