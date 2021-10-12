from src.readers.i_csv_reader import ICSVReader
from src.readers.i_txt_reader import ITXTReader

class CSVReaderAdapter(ICSVReader, ITXTReader):

    def __init__(self, reader):
        self.reader = reader()

    def read_csv_file(self, filename):
        csvWords = self.reader.read_csv_file(filename)
        return csvWords[0][:-2].split(',')

    def read_txt_file(self, filename):
        pass
