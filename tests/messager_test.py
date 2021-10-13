import pytest
from unittest.mock import Mock, MagicMock
from unittest.mock import patch, call

from src.message_sender import MessageSender

@patch('builtins.print')
def test_that_sends_message(mocked_print):
    # Arrange
    ms = MessageSender()

    ms.send("Bob", "Test")
    assert mocked_print.mock_calls == [call('Sending "Test" to Bob')]
