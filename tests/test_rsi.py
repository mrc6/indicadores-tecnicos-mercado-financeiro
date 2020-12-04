import modules
from project import rsi
from decimal import Decimal


print(modules)

# variável do escopo global
TWOPLACES = Decimal(10) ** -2


def test_if_get_gain_loses_returns_correct_value():
    "Teste se a função get_gain_loses retorna o valor correto"
    data = [
        ['1365752460', '82'],
        ['1365752520', '81.78'],
        ['1365752580', '84.25'],
        ['1365752640', '83.48']
    ]
    result = [
        ['1365752460', '82', 0, 0],
        ['1365752520', '81.78', 0, Decimal('0.22')],
        ['1365752580', '84.25', Decimal('2.47'), 0],
        ['1365752640', '83.48', 0, Decimal('0.77')]
    ]
    assert rsi.get_gains_losses(data, 1) == result


def test_if_first_rsi_returns_correct_value():
    "Testa se a funcao first_rsi retorna o valor correto"
    data = [
        ['1365752460', Decimal('82.00'), 0, 0],
        ['1365752520', Decimal('81.78'), 0, Decimal('0.22')],
        ['1365752580', Decimal('84.25'), Decimal('2.47'), 0],
        ['1365752640', Decimal('83.48'), 0, Decimal('0.77')]
    ]
    result = {'f_g_sma': Decimal('1.24'), 'f_l_sma': Decimal('0.11')}
    assert rsi.first_rsi(data, 2, 2, 3) == result


def test_if_table_with_first_rsi_returns_correct_value():
    "Testa se a função table_with_first_rsi retorna o valor correto"
    data = [
        ['1365752460', '80.01', 0, 0, 0],
        ['1365752520', Decimal('82.00'), Decimal('81.00'), Decimal('1.99'), 0],
        ['1365752580', '83.48', '82.65', '1.48', 0],
        ['1365752640', '83.48', '83.20', 0, 0]
    ]
    gl = {'gsma': Decimal('1.74'), 'lsma': Decimal('0.87')}
    result = [
        ['1365752460', '80.01', 0, 0, 0, '', ''],
        [
            '1365752520',
            Decimal('82.00'),
            Decimal('81.00'),
            Decimal('1.99'),
            0,
            '',
            ''
        ],
        [
            '1365752580',
            '83.48',
            '82.65',
            '1.48',
            0,
            Decimal('1.74'),
            Decimal('0.87')
        ],
        ['1365752640', '83.48', '83.20', 0, 0, '', '']
    ]
    assert rsi.table_with_first_rsi(data, 2, gl["gsma"], gl["lsma"]) == result


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


def test_if_calc_rsi_returns_currect_value():
    "Testa se a funcao calc_rsi retorna os valores corretos"
    result = Decimal('54.55').quantize(TWOPLACES)
    calc = Decimal(rsi.calc_rsi(1.2)).quantize(TWOPLACES)
    assert calc == result


def test_if_table_with_avgs_returns_correct_value():
    "Testa se a função table_with_avgs retorna os valores corretos"
    data = [
        ['1365752460', '80.01', "", "", "", ""],
        [
            '1365752520',
            '82.00',
            '81.00',
            '1.99',
            0,
            ""
        ],
        [
            '1365752580',
            '83.48',
            '82.65',
            '1.48',
            0,
            '1.74'
        ],
        ['1365752640', '83.48', '83.20', 0, 0, ""]
    ]
    result = [
        ['1365752460', '80.01', '', '', '', ''],
        ['1365752520', '82.00', '81.00', '1.99', 0, ''],
        ['1365752580', '83.48', '82.65', '1.48', 0, '1.74'],
        ['1365752640', '83.48', '83.20', 0, 0, Decimal('0.87')],
    ]
    result2 = [
        ['1365752460', '80.01', '', '', '', ''],
        ['1365752520', '82.00', '81.00', '1.99', 0, ''],
        ['1365752580', '83.48', '82.65', '1.48', 0, '1.74'],
        ['1365752640', '83.48', '83.20', 0, 0, Decimal('0.87')],
    ]
    assert rsi.table_with_avgs(data, 2, 5) == result
    assert rsi.table_with_avgs(result, 2, 5) == result2


def test_if_table_with_rs_returns_correct_values():
    data = [
        ['1365752460', '80.01', '', '', '', '', ''],
        ['1365752520', '82.00', '81.00', '1.99', 0, '', ''],
        ['1365752580', '83.48', '82.65', '1.48', 0, '1.74', 0],
        ['1365752640', '83.48', '83.20', 0, 0, Decimal('0.87'), 0],
    ]
    result = [
        ['1365752460', '80.01', '', '', '', '', '', ''],
        ['1365752520', '82.00', '81.00', '1.99', 0, '', '', ''],
        [
            '1365752580',
            '83.48',
            '82.65',
            '1.48',
            0,
            '1.74',
            0,
            Decimal('1000000.00')
        ],
        [
            '1365752640',
            '83.48',
            '83.20',
            0,
            0,
            Decimal('0.87'),
            0,
            Decimal('1000000.00')
        ],
    ]
    assert rsi.table_with_rs(data, 2, 5) == result


def test_if_table_with_rsi_returns_correct_values():
    data = [
        ['1365752460', '80.01', '', '', '', '', '', ''],
        ['1365752520', '82.00', '81.00', '1.99', 0, '', '', ''],
        [
            '1365752580',
            '83.48',
            '82.65',
            '1.48',
            0,
            '1.74',
            0,
            '1000000.00'
        ],
        [
            '1365752640',
            '83.48',
            '83.20',
            0,
            0,
            '0.87',
            0,
            '1000000.00'
        ],
    ]

    result = [
        ['1365752460', '80.01', '', '', '', '', '', '', ''],
        ['1365752520', '82.00', '81.00', '1.99', 0, '', '', '', ''],
        [
            '1365752580',
            '83.48',
            '82.65',
            '1.48',
            0,
            '1.74',
            0,
            '1000000.00',
            Decimal('100.00')
        ],
        [
            '1365752640',
            '83.48',
            '83.20',
            0,
            0,
            '0.87',
            0,
            '1000000.00',
            Decimal('100.00')
        ]
    ]
    assert rsi.table_with_rsi(data, 2, 7) == result
