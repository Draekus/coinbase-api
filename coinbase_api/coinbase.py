"""Main Coinbase API module."""

import hmac
import hashlib
import time
from requests.auth import AuthBase


class CoinbaseWalletAuth(AuthBase):
    """Generate Coinbase API authentication headers."""

    def __init__(self, api_key, secret_key, api_version):
        self.api_key = api_key
        self.secret_key = secret_key
        self.api_version = api_version

    def __call__(self, request):
        timestamp = str(int(time.time()))
        message = timestamp + request.method + request.path_url + (request.body or "")
        signature = hmac.new(
            self.secret_key.encode(), message.encode(), hashlib.sha256
        ).hexdigest()

        request.headers.update(
            {
                "CB-ACCESS-SIGN": signature,
                "CB-ACCESS-TIMESTAMP": timestamp,
                "CB-ACCESS-KEY": self.api_key,
                "CB-VERSION": self.api_version,
            }
        )
        return request


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
