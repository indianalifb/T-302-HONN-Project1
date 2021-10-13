
from src.merch.Imerch import Imerch

class MercheDecorator(Imerch):
    _wrapeee: Imerch = None
    
    def __init__(self, imerch: Imerch) -> None:
        self._wrapeee = imerch

    def getDescription(self):
        return self._wrapeee.getDescription()

    def cost(self):
        return self._wrapeee.cost()

    


