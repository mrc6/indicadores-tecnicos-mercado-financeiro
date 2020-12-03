# interface de comunicação com o trader
from datetime import datetime
from os import system, name
from utils import load_defs, change_defs
from do_rel import write_csv_file


# Ref.: https://www.geeksforgeeks.org/clear-screen-python/
# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def date_verify(date):
    d_check = date
    while d_check[2] != "-" or d_check[5] != "-" or len(d_check) != 10:
        print("Data informada é inválida, digite novamente ")
        d_check = input("Digite a Data Anterior (DD-MM-AAAA): ")
    year = int(d_check[6:10])
    month = int(d_check[3:5])
    day = int(d_check[0:2])
    return datetime(year, month, day, 00, 00, 00, 000000)


def verify_input_is_number(text):
    while True:
        try:
            n = int(input(text))
            return n
            break
        except ValueError:
            print("Digite apenas números")


# variáveis do escopo global


def menu():
    option = 0
    while option != 9:
        clear()
        print("Bem Vindo ao Sistema de Informações Sobre o Mercado")
        print("Selecione uma opção:")
        print("1 - Criar Relatorio MME + IFR")
        print("2 - Mostrar Configurações dos Indicadores")
        print("3 - Alterar Configurações dos Indicadores")
        print("9 - Sair")
        option = verify_input_is_number("Digite a opção escolhida: ")
        if option == 1:
            clear()
            start_date = date_verify(
                input("Digite a Data Inicial Escolhida (DD-MM-AAAA): ")
            )
            end_date = date_verify(
                input("Digite a Data Final Escolhida (DD-MM-AAAA): ")
            )
            print("Criando o Relatório...(Isso pode demorar alguns minutos)")
            write_csv_file(start_date, end_date)
            input("Digite ENTER Para Voltar ao Menu Principal")
        if option == 2:
            clear()
            defs = load_defs()

            print("Informações dos Indicadores Técnicos")
            print(f'Periodo da MME: {defs["ema_period"]}')
            print(f'Periodo da IRF: {defs["rsi_p"]}')
            if defs["price_c"] == 1:
                print("Preço Usado para o Cálculo: ABERTURA")
            if defs["price_c"] == 2:
                print("Preço Usado para o Cálculo: MÁXIMO")
            if defs["price_c"] == 3:
                print("Preço Usado para o Cálculo: MÍNIMO")
            if defs["price_c"] == 4:
                print("Preço Usado para o Cálculo: FECHAMENTO")
            input("Digite ENTER Para Voltar ao Menu Principal")
        if option == 3:
            clear()
            ema_p = verify_input_is_number("Digite o Novo Período da MME: ")
            rsi_p = verify_input_is_number("Digite o Novo Período da IRF: ")
            print("Digite o Tipo de Preço Para Cálculo:")
            print("1 - ABERTURA")
            print("2 - MÁXIMO")
            print("3 - MÍNIMO")
            print("4 - FECHAMENTO")
            np = 5
            while np >= 5 or np == 0:
                np = verify_input_is_number("Digite o Número do Novo Preço: ")
            change_defs(ema_p, rsi_p, np)
            input("Digite ENTER Para Voltar ao Menu Principal")


menu()
