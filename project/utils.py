import csv
import json
from decimal import Decimal
from datetime import datetime
import re


# função para carregar as definições de operação
def load_defs():
    with open("definitions.json") as file:
        # leitura do arquivo
        content = file.read()
        # o conteúdo é transformado
        # em estrutura python equivalente, dicionário neste caso.
        return json.loads(content)


def change_defs(ema_p, rsi_p, price):
    defs = load_defs()
    defs["ema_period"] = ema_p
    defs["rsi_p"] = rsi_p
    defs["price_c"] = price
    with open("definitions.json", "w") as file:
        json_to_write = json.dumps(defs)
        file.write(json_to_write)


# função muda notação de número no formato nnn,nn
def change_notation(num):
    if type(num) is Decimal or type(num) is int:
        return num
    number = num
    index = 0
    len_n = len(number)
    for character in number:
        if character == ",":
            index = number.index(character)
    if index != 0:
        return Decimal(number[0: index] + "." + number[index + 1: len_n])
    else:
        return Decimal(number)


# função para limpar os dados
def clear_memory():
    for name in dir():
        if not name.startswith('_'):
            del globals()[name]


def read_file(location):
    with open(location) as file:
        file_status_reader = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = file_status_reader
    return {"data": data, "header": header}


def slice_data(data, start_date, end_date):
    defs = load_defs()
    d_time = datetime.fromtimestamp
    sliced_data = []
    for col in data:
        if start_date <= d_time(int(col[defs["tstp_col"]])) <= end_date:
            sliced_data.append([col[defs["tstp_col"]], col[defs["price_c"]]])
    return sliced_data


def clear_data(sliced_data):
    defs = load_defs()
    result = []
    for col in sliced_data:
        if len(col[defs["tstp_col"]]) == 10 and col[defs["c_price"]] != "NaN":
            col[defs["c_price"]] = change_notation(
                col[defs["c_price"]]
            )
            result.append(col)
    return result


# recebe o valor numerico de um mes no format Sss
def get_integer_from_month(str):
    result = ""
    if re.search("Jan", str):
        result = 1
    elif re.search("Feb", str):
        result = 2
    elif re.search("Mar", str):
        result = 3
    elif re.search("Apr", str):
        result = 4
    elif re.search("May", str):
        result = 5
    elif re.search("Jun", str):
        result = 6
    elif re.search("Jul", str):
        result = 7
    elif re.search("Aug", str):
        result = 8
    elif re.search("Sep", str):
        result = 9
    elif re.search("Oct", str):
        result = 10
    elif re.search("Nov", str):
        result = 11
    else:
        result = 12
    return result


# transforma uma dada no formato dd-Mmm-yy em dateTime
def get_date(str):
    d_check = str
    if len(d_check) == 9:
        if d_check[2] != "-" or d_check[6] != "-":
            print("Data informada é inválida")
        year = int(d_check[7:9]) + 2000
        tmp_month = (d_check[3:6])
        month = get_integer_from_month(tmp_month)
        day = int(d_check[0:2])
    if len(d_check) == 8:
        if d_check[1] != "-" or d_check[5] != "-":
            print("Data informada é inválida")
        year = int(d_check[6:8]) + 2000
        tmp_month = (d_check[2:5])
        month = get_integer_from_month(tmp_month)
        day = int(d_check[0])
    return datetime(year, month, day, 00, 00, 00, 000000)
