"""
This module is for testing server
"""
from server.server import receive_message, add_numbers


def test_receive_message():
    """This function tests receiving a message"""
    assert receive_message('Hello, World!') == 'Hello, World!'


def test_add_numbers():
    """This function tests adding numbers"""
    assert add_numbers(2, 10) == 12
