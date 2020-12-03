import modules
from project import rsi
from decimal import Decimal


print(modules)

# variável do escopo global
TWOPLACES = Decimal(10) ** -2


def test_if_get_gain_loses_returns_correct_value():
    "Teste se a função get_gain_loses retorna o valor correto"
    data = [
        ["1365752520", Decimal(82).quantize(TWOPLACES)],
        ["1365752580", Decimal(81.78).quantize(TWOPLACES)],
        ["1365752580", Decimal(84.25).quantize(TWOPLACES)],
        ["1365752580", Decimal(83.48).quantize(TWOPLACES)]
    ]
    result = [
        ['1365752520', Decimal('82.00'), 0, 0],
        ['1365752580', Decimal('81.78'), 0, Decimal('81.78')],
        ['1365752580', Decimal('84.25'), Decimal('84.25'), 0],
        ['1365752580', Decimal('83.48'), 0, Decimal('83.48')]
    ]
    assert rsi.get_gains_losses(data, 1) == result


def test_if_first_rsi_returns_correct_value():
    "Testa se a funcao first_rsi retorna o valor correto"
    data = [
        ['1365752520', Decimal('82.00'), 0, 0],
        ['1365752580', Decimal('81.78'), 0, Decimal('81.78')],
        ['1365752580', Decimal('84.25'), Decimal('84.25'), 0],
        ['1365752580', Decimal('83.48'), 0, Decimal('83.48')]
    ]
    result = {'f_g_sma': Decimal('21.06'), 'f_l_sma': Decimal('41.32')}
    assert rsi.first_rsi(data, 4, 2, 3) == result


def test_if_table_with_first_rsi_returns_correct_value():
    "Testa se a função table_with_first_rsi retorna o valor correto"
    data = [
        ['1365752520', Decimal('82.00'), 0, 0],
        ['1365752580', Decimal('81.78'), 0, Decimal('81.78')],
        ['1365752580', Decimal('84.25'), Decimal('84.25'), 0],
        ['1365752580', Decimal('83.48'), 0, Decimal('83.48')]
    ]
    gl = {'gsma': Decimal('21.06'), 'lsma': Decimal('41.32')}
    result = [
        ['1365752520', Decimal('82.00'), 0, 0, '', ''],
        ['1365752580', Decimal('81.78'), 0, Decimal('81.78'), '', ''],
        ['1365752580', Decimal('84.25'), Decimal('84.25'), 0, '', ''],
        [
            '1365752580',
            Decimal('83.48'),
            0,
            Decimal('83.48'),
            Decimal('21.06'),
            Decimal('41.32')
        ]
    ]
    assert rsi.table_with_first_rsi(data, 4, gl["gsma"], gl["lsma"]) == result


def test_if_calc_avgs_return_currect_value():
    "Testa se a função calc_avgs retorna os valores corretos"
    last_rsi = Decimal('21.06').quantize(TWOPLACES)
    actual_diff = Decimal('0.18').quantize(TWOPLACES)
    period = 4
    result = Decimal('15.98').quantize(TWOPLACES)
    calc = rsi.calc_avgs(last_rsi, actual_diff, period).quantize(TWOPLACES)
    assert calc == result


def test_if_calc_rs_returns_currect_value():
    "Testa se a funcao calc_rs retorna os valores corretos"
    avg_g = Decimal('21.06').quantize(TWOPLACES)
    avg_l = Decimal('19.18').quantize(TWOPLACES)
    result = Decimal('1.10').quantize(TWOPLACES)
    assert rsi.calc_rs(avg_g, avg_l).quantize(TWOPLACES) == result
