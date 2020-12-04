import csv
from utils import read_file, load_defs, clear_memory
from ema import return_file_with_ema
from rsi import return_file_with_ema_rsi


def write_csv_file(s_date, e_date):
    defs = load_defs()
    # lendo o cabeçalho do arquivo pai
    header = read_file(defs["f_path"])["header"]
    # abre um arquivo para escrita
    with open("../data/rel.csv", "w", newline="") as file:
        # configurações da EMA
        path = defs["f_path"]
        period = defs["ema_period"]
        price_c = defs["c_price"]

        # variável com a tabela da EMA
        ema_table = return_file_with_ema(path, period, price_c, s_date, e_date)
        # variável com a tabela com EMA + RSI
        result = return_file_with_ema_rsi(ema_table)

        # É necessário passar o arquivo e o cabeçalho
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        # escreve as linhas de dados
        # este é o cabeçalho
        writer.writerow([
            header[0],
            header[defs["price_c"]],
            f'EMA({defs["ema_period"]})',
            f'RSI({defs["rsi_p"]})'
        ])
        # estes são os dados
        for lines in result:
            writer.writerow(lines[0:3] + [lines[8]])
    print("Relatório Criado!")
    clear_memory()
