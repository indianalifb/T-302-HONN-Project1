from abc import ABC, abstractmethod
from typing import List

class ITXTReader(ABC):
    @abstractmethod
    def read_txt_file(self, filename: str) -> List[str]:
        pass
