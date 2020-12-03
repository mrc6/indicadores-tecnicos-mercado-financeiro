import modules
import pytest
import json
from datetime import datetime
from decimal import Decimal
from project import utils
# from project.utils import load_defs
from unittest.mock import mock_open, patch


print(modules)

# variável do escopo global
TWOPLACES = Decimal(10) ** -2


@pytest.fixture
def mock_defs():
    return {
        "f_path": "../data/dont_care.csv",
        "ema_period": 10,
        "c_price": 1,
        "tstp_col": 0,
        "price_c": 4,
        "rsi_p": 14,
        "gci": 3,
        "lci": 4,
        "avg_gci": 5,
        "avg_lci": 6,
        "rs_c": 7
    }


def test_change_notation_returns_decimal_number():
    "Teste se a função change_notation retorna um número decimal"
    case_1 = utils.change_notation("70.01").quantize(TWOPLACES)
    case_2 = Decimal(70.01).quantize(TWOPLACES)
    assert case_1 == case_2


def test_slice_date(mock_defs):
    "Teste se a função slice_data retorna os dados corretos"
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_defs))):
        data = [
            [1365752460, "82", "82", "80,01", "80,01"],
            [1365752520, "82", "82", "82", "82"],
            [1365752580, "83,4", "83,48", "83,4", "83,48"],
            [1365752640, "83,47", "83,48", "83,47", "83,48"]
        ]
        result = [[1365752520, '82'], [1365752580, '83,48']]
        start_date = datetime.fromtimestamp(1365752520)
        end_date = datetime.fromtimestamp(1365752580)
        assert utils.slice_data(data, start_date, end_date) == result
