# importando os modulos necessarios para o projeto
from decimal import Decimal
from datetime import datetime
from utils import change_notation, read_file, clear_data, slice_data

# referência para os cálculos
#  https://www.bussoladoinvestidor.com.br/media-movel-exponencial/

# variáveis no escopo global
result = []
TWOPLACES = Decimal(10) ** -2
d_time = datetime.fromtimestamp


def get_sma(data, period, collumn_index):
    loop = 0
    sma = 0
    for collumn in data:
        if loop < period:
            sma = sma + change_notation(collumn[collumn_index])
            loop += 1
        if loop == period:
            return (sma / period).quantize(TWOPLACES)


# abrindo os dados do arquivo csv
def data_with_first_sma(location, period, collumn_index, s_date, e_date):
    print("Abrindo o Arquivo de Dados...")
    data = read_file(location)["data"]
    n = 0
    result = []
    print("Selecionando os Dados Pela Data...")
    filtered_data = slice_data(data, s_date, e_date)
    print("Limpando Dados Inválidos...")
    cleaned_data = clear_data(filtered_data)
    sma = get_sma(cleaned_data, period, collumn_index)
    print("Calculando a MME...")
    for collumn in cleaned_data:
        if n < period - 1:
            result.append(collumn + [""])
        if n == period - 1:
            result.append(collumn + [sma])
        if n > period - 1:
            result.append(collumn + [""])
        n += 1
    return result


def ema_calc(last_ema, actual_price, period):
    ema = (actual_price - last_ema) * Decimal((2/(period + 1))) + last_ema
    return ema


def return_file_with_ema(location, period, cidx, s_date, e_date):
    original_data = data_with_first_sma(location, period, cidx, s_date, e_date)
    calc_data = []
    loop = 0
    last_ema = 0
    actual_ema = 0
    for prices in original_data:
        # quando achar a primeira sma
        if prices[2]:
            break
        loop += 1
    # cria o arquivo de saida
    for prices in original_data:
        if original_data.index(prices) < loop:
            calc_data.append(prices[0:2] + [""])
        if original_data.index(prices) == loop + 1:
            last_ema = original_data[original_data.index(prices)-1][2]
            actual_price = change_notation(prices[1])
            actual_ema = ema_calc(last_ema, actual_price, period)
            calc_data.append(prices[0:2] + [actual_ema.quantize(TWOPLACES)])
            last_ema = actual_ema
        if original_data.index(prices) > loop + 1:
            actual_price = change_notation(prices[1])
            actual_ema = ema_calc(last_ema, actual_price, period)
            calc_data.append(prices[0:2] + [actual_ema.quantize(TWOPLACES)])
            last_ema = actual_ema
    return calc_data
