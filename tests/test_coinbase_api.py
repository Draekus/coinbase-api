"""Tests for coinbase_api.py"""

from dotenv import dotenv_values
import requests
from coinbase_api import __version__
from coinbase_api.coinbase import CoinbaseWalletAuth


# Load environment variables from .env
config = dotenv_values(".env")

# Set API key and secret
API_KEY = config["API_KEY"]
API_SECRET = config["API_SECRET"]
API_VERSION = config["API_VERSION"]


def test_version():
    """Test the module's version."""
    assert __version__ == "0.1.0"


def test_get_user():
    """Test get_user function."""
    # Set API URL
    api_url = "https://api.coinbase.com/v2/"
    # Generate auth headers
    auth = CoinbaseWalletAuth(API_KEY, API_SECRET, API_VERSION)

    # Get current user
    r = requests.get(api_url + "user", auth=auth, timeout=5)

    # Get status code
    status_code = r.status_code

    # Test status code
    assert status_code == 200
