"""
This module is for testing server
"""
from server.server import receive_message


def test_receive_message():
    """This function tests receiving a message"""
    assert receive_message('Hello, World!') == 'Hello, World!'
