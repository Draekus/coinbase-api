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


# Set API URL
api_url = "https://api.coinbase.com/v2/"
# Generate auth headers
auth = CoinbaseWalletAuth(API_KEY, API_SECRET, API_VERSION)

# Get current user
r = requests.get(api_url + "user", auth=auth, timeout=5)
userID = r.json()["data"]["id"]
print(r.json())

api_url = "https://api.coinbase.com/v2/accounts/" + userID + "/addresses"
r = requests.get(api_url, auth=auth, timeout=5)
print(r.status_code)
print(r.json())
