"""Main Coinbase API module."""

import hmac, hashlib, time
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
