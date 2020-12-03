import modules
from project import ema
from decimal import Decimal


print(modules)

# variável do escopo global
TWOPLACES = Decimal(10) ** -2


def test_if_get_sma_returns_correct_value():
    "Teste se a função get_sma retorna o valor correto"
    data = [
        ["1365752520", Decimal(82).quantize(TWOPLACES)],
        ["1365752580", Decimal(81.78).quantize(TWOPLACES)],
        ["1365752580", Decimal(84.25).quantize(TWOPLACES)],
        ["1365752580", Decimal(83.48).quantize(TWOPLACES)]
    ]
    assert ema.get_sma(data, 4, 1) == Decimal(82.88).quantize(TWOPLACES)


def test_if_ema_calc_returns_correct_value():
    "Testa se a funcao ema_calc retorna o valor correto"
    actual_price = Decimal(82.48).quantize(TWOPLACES)
    last_ema = Decimal(83.10).quantize(TWOPLACES)
    result = Decimal(82.79).quantize(TWOPLACES)
    assert ema.ema_calc(last_ema, actual_price, 3) == result
