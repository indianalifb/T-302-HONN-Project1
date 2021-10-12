from abc import ABC, abstractmethod
from typing import List

class ICSVReader(ABC):
    @abstractmethod
    def read_csv_file(self, filename: str) -> List[str]:
        pass
