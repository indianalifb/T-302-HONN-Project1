from unittest.mock import Mock, MagicMock

import pytest

from src.reader import Reader
from src.readers.csv_reader import CSVReader
from src.readers.txt_reader import TXTReader
from src.readers.csv_reader_adapter import CSVReaderAdapter

def test_that_txt_reader_returns_a_list_of_strings():
    # Arrange
    txt_reader = TXTReader()

    # Act
    words = txt_reader.read_txt_file(filename = 'src/WordData/Animals/Easyanimals.txt')

    # assert
    assert type(words) == list
    assert type(words[0]) == str

def test_theat_csv_reader_returns_a_list_of_strings():
    # arrange
    csv_reader = CSVReader()

    # Act
    words = csv_reader.read_csv_file(filename = 'src/WordData/Countries/Easycountries.csv')

    # assert

    assert type(words) == list
    assert type(words[0]) == str

def test_that_csv_reader_adapter_returns_list_of_strings():
    # arrange
    csv_reader = MagicMock(CSVReader())
    csv_reader.return_value.read_csv_file.return_value = ["String1", "String2"]
    adapter = CSVReaderAdapter(csv_reader)

    # act
    words = adapter.read_csv_file('src/WordData/Countries/Easycountries.csv')

    # assert
    assert type(words) == list
    assert type(words[0]) == str



def test_that_reader_returns_a_string():
    # arrange
    txt_reader = Mock(TXTReader())
    adapter = CSVReaderAdapter(CSVReader)
    reader = Reader(txt_reader, adapter)

    # Act Assert
    wrds = reader.get_words('c', 'e')

    # Assert
    assert type(wrds) == str

def test_that_reader_is_randomized():
    # Arrange
    txt_reader = TXTReader()
    csv_reader = Mock(CSVReader())
    adapter = Mock(CSVReaderAdapter(csv_reader))
    reader = Reader(txt_reader, adapter)


    # Act
    word_1 = reader.get_words('a', 'e')
    word_2 = reader.get_words('a', 'e')

    # Assert
    assert word_1 is not word_2

def test_that_csv_reader_throws_exception_with_bad_filename():
    # Arrangu
    csv_reader = CSVReader()

    # Act Assert
    with pytest.raises(FileNotFoundError) as exception:
        csv_reader.read_csv_file("bro")

def test_that_txt_reader_throws_exception_with_bad_filename():
    # arrange
    txt_reader = TXTReader()

    # Act Assert
    with pytest.raises(FileNotFoundError) as exception:
        txt_reader.read_txt_file("son")

def test_that_adapter_read_txt_file_returns_nothing():
    # Arrange
    reader = Mock(CSVReader())
    adapter = CSVReaderAdapter(reader)
    # Act
    words = adapter.read_txt_file("")
    # assert
    assert words is None

def test_that_adapter_throws_exception_on_bad_filename():
    # Arrange
    reader = CSVReader
    adapter = CSVReaderAdapter(reader)
    # Act Assert
    with pytest.raises(FileNotFoundError) as exception:
        adapter.read_csv_file("bro")
