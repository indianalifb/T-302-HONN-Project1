from merch.Imerch import Imerch
from merch.merch_decorator import MercheDecorator

class PrintName(MercheDecorator):

    def getDescription(self):
        return f"{self._wrapeee.getDescription()} with your name"

    def cost(self):
        return self._wrapeee.cost() + 300
