from src.readers.i_txt_reader import ITXTReader
from typing import List

class TXTReader(ITXTReader):
    def read_txt_file(self, filename: str) -> List[str]:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f]
            return lines
