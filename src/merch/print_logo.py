
from src.merch.merch_decorator import MercheDecorator

class PrintLogo(MercheDecorator):
    #add description to pants/sweater description
    def getDescription(self):
        return f"{self._wrapeee.getDescription()} with our logo"

    #add cost to the sweater/pants cost
    def cost(self):
        return self._wrapeee.cost() + 500
        