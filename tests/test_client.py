"""
This module is for testing client
"""

from client.client import send_message


def test_send_message():
    """This function tests send_message"""
    assert send_message('Hello, World!') == 'Hello, World!'
