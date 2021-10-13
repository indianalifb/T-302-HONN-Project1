import pytest
from unittest.mock import Mock, MagicMock
from unittest.mock import patch, call

from src.buy_merch import BuyMerch
from src.merch.pants import Pants
from src.merch.sweater import Sweater

@patch('builtins.print')
def test_that_purchases_pants(mocked_print):
    # Arrange
    buy = BuyMerch()
    clothes = Pants()

    buy.purchase(clothes)
    assert mocked_print.mock_calls == [call("*** You bought: Pants for 4000 kr ***")]

@patch('builtins.print')
def test_that_purchases_sweater(mocked_print):
    # Arrange
    buy = BuyMerch()
    clothes = Sweater()

    buy.purchase(clothes)
    assert mocked_print.mock_calls == [call("*** You bought: Sweater for 3000 kr ***")]

