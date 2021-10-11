

from merch.Imerch import Imerch
from merch.sweater import Sweater
from merch.print_name import PrintName
from merch.print_logo import PrintLogo

def client_code(imerch: Imerch) -> None:
    print(f"RESULT: {imerch.cost()}", end="")


simple = Sweater()

client_code(simple)
print()

swater_name = PrintName(simple)
sweater_logo = PrintLogo(swater_name)
client_code(sweater_logo)