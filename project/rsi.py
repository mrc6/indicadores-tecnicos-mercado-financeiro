import modules
from decimal import Decimal
from project.utils import change_notation, load_defs
from project.ema import get_sma

assert modules
# Referência para os cálculos https://bit.ly/3qexPil

# variáveis no escopo global
TWOPLACES = Decimal(10) ** -2
# carrega as definições
# defs = load_defs()


def get_gains_losses(data, collumn_index):
    loop = 0
    gain = []
    losses = []
    last_price = 0
    result = []
    for collumn in data:
        if loop == 0:
            last_price = change_notation(collumn[collumn_index])
            result.append(collumn + [0] + [0])
        if loop > 0:
            if change_notation(collumn[collumn_index]) - last_price > 0:
                gain = change_notation(collumn[collumn_index] - last_price)
                last_price = change_notation(collumn[collumn_index])
                result.append(collumn + [gain] + [0])
            elif change_notation(collumn[collumn_index]) - last_price < 0:
                losses = change_notation(last_price - collumn[collumn_index])
                last_price = change_notation(collumn[collumn_index])
                result.append(collumn + [0] + [losses])
            else:
                last_price = change_notation(collumn[collumn_index])
                result.append(collumn + [0] + [0])
        loop += 1
    return result


def first_rsi(data, period, g_col_idx, l_col_idx):
    ignore_1st, *table = data  # ignora a primeira linha, sem ganhos / perdas
    f_g_sma = get_sma(table, period, g_col_idx)
    f_l_sma = get_sma(table, period, l_col_idx)
    return {"f_g_sma": f_g_sma, "f_l_sma": f_l_sma}


def table_with_first_rsi(data, period, rsi_g, rsi_l):
    result = []
    n = 1  # ignora a primeira linha pois não tem ganhos / perdas
    for collumn in data:
        if n <= period:
            result.append(collumn + [""] + [""])
        if n == period + 1:
            result.append(collumn + [rsi_g] + [rsi_l])
        if n > period + 1:
            result.append(collumn + [""] + [""])
        n += 1
    return result


def calc_avgs(last_rsi, actual_diff, period):
    rs = actual_diff + (last_rsi * (period - 1)) / period
    return rs


def calc_rs(avg_g, avg_l):
    rs = avg_g / avg_l
    return rs


def calc_rsi(rs):
    rsi = 100 - (100 / (1 + rs))
    return rsi


def table_with_avgs(data, period, collumn_index):
    calc_data = []
    loop = 0
    last_avg = 0
    actual_avg = 0
    for prices in data:
        # quando achar a primeira avg
        if prices[collumn_index] >= 0:
            break
        loop += 1
    # cria o arquivo de saida
    for prices in data:
        if data.index(prices) < loop + 1:
            calc_data.append(prices)
        if data.index(prices) == loop + 1:
            last_avg = data[data.index(prices)-1][collumn_index]
            actual_price = change_notation(prices[collumn_index - 2])
            actual_avg = calc_avgs(last_avg, actual_price, period)
            calc_data.append(
                prices[0:collumn_index] + [actual_avg.quantize(TWOPLACES)]
            )
            last_avg = actual_avg
        if data.index(prices) > loop + 1:
            actual_price = change_notation(prices[collumn_index - 2])
            actual_avg = calc_avgs(last_avg, actual_price, period)
            calc_data.append(
                prices[0:collumn_index] + [actual_avg.quantize(TWOPLACES)]
            )
            last_avg = actual_avg
    return calc_data


def table_with_rs(data, period, collumn_index):
    calc_data = []
    loop = 0
    rs = 0
    for prices in data:
        # quando achar a primeira avg
        if prices[collumn_index]:
            break
        loop += 1
    # cria o arquivo de saida
    for prices in data:
        if data.index(prices) < loop:
            calc_data.append(prices + [""])
        if data.index(prices) >= loop:
            rs = calc_rs(prices[collumn_index], prices[collumn_index + 1])
            calc_data.append(
                prices[0:collumn_index + 2] + [rs.quantize(TWOPLACES)]
            )
    return calc_data


def table_with_rsi(data, period, collumn_index):
    calc_data = []
    loop = 0
    rsi = 0
    for prices in data:
        # quando achar o primeiro rs
        if prices[collumn_index]:
            break
        loop += 1
    # cria o arquivo de saida
    for prices in data:
        if data.index(prices) < loop:
            calc_data.append(prices + [""])
        if data.index(prices) >= loop:
            rsi = calc_rsi(prices[collumn_index])
            calc_data.append(
                prices[0:collumn_index + 1] + [rsi.quantize(TWOPLACES)]
            )
    return calc_data


def return_file_with_ema_rsi(data):
    defs = load_defs()
    # transformação RSI
    print("Calculando o IFR...")
    m_table = get_gains_losses(data, defs["c_price"])
    rsi = first_rsi(m_table, defs["rsi_p"], defs["gci"], defs["lci"])
    rsi_g = rsi["f_g_sma"]
    rsi_l = rsi["f_l_sma"]
    m_2_table = table_with_first_rsi(m_table, defs["rsi_p"], rsi_g, rsi_l)
    m_3_table = table_with_avgs(m_2_table, defs["rsi_p"], defs["avg_gci"])
    m_4_table = table_with_avgs(m_3_table, defs["rsi_p"], defs["avg_lci"])
    return m_4_table
    m_5_table = table_with_rs(m_4_table, defs["rsi_p"], defs["avg_gci"])
    return table_with_rsi(m_5_table, defs["rsi_p"], defs["rs_c"])
