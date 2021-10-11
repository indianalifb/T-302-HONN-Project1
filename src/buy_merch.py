

from src.merch.merch_decorator import MercheDecorator
from src.merch.print_logo import PrintLogo
from src.merch.print_name import PrintName
from src.merch.Imerch import Imerch

from src.merch.pants import Pants
from src.merch.sweater import Sweater

class BuyMerch:
    def purchase(self,clothes : Imerch):
        self.client_code(clothes)



    def client_code(self,imerch: Imerch) -> None:
        print(f"*** You bought: {imerch.getDescription()} for {imerch.cost()} kr ***")