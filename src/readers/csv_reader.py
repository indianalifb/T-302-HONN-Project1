from typing import List
from src.readers.i_csv_reader import ICSVReader

class CSVReader(ICSVReader):
    def read_csv_file(self, filename: str) -> List[str]:
        with open(filename) as file:
            words = []
            for line in file:
                words.append(line)

            return words
