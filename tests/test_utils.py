import modules
from decimal import Decimal
from project import utils

print(modules)

# variável do escopo global
TWOPLACES = Decimal(10) ** -2

def test_change_notation_returns_decimal_number():
    "Teste se a função change_notation retorna um número decimal"
    assert utils.change_notation("70.01").quantize(TWOPLACES) == Decimal(70.01).quantize(TWOPLACES)
