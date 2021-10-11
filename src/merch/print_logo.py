from merch.Imerch import Imerch
from merch.merch_decorator import MercheDecorator

class PrintLogo(MercheDecorator):
    def getDescription(self):
        return f"{self._wrapeee.getDescription()} with our logo"

    def cost(self):
        return self._wrapeee.cost() + 500
        