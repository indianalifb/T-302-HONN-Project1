

from src.merch.merch_decorator import MercheDecorator
from src.merch.print_logo import PrintLogo
from src.merch.print_name import PrintName
from src.merch.Imerch import Imerch

from src.merch.pants import Pants
from src.merch.sweater import Sweater

class BuyMerch:
    #print out the descripton and cost of the clothes bought and logo/name if that added
    def purchase(self,imerch : Imerch):
        print(f"*** You bought: {imerch.getDescription()} for {imerch.cost()} kr ***")
