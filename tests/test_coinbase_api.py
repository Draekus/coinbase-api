"""Tests for coinbase_api.py"""

from coinbase_api import __version__


def test_version():
    """Test the module's version."""
    assert __version__ == "0.1.0"
