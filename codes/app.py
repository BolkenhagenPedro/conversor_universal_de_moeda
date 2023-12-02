from forex_python.converter import CurrencyRates

def limpar_terminal():
    from os import system
    from platform import system as sys

    op = sys()
    if op == 'Windows': system('cls')
    else: system('clear')

def converter(valor, moeda_origem, moeda_destino):
    while True:
        try:
            c = CurrencyRates()
            taxa = c.get_rate(moeda_origem, moeda_destino)
            valor = valor * taxa
            return valor
        except:
            print('Digitaste uma moeda que não existe. Digita um válida...')
            moeda_origem = input('Moeda de origem: ')
            moeda_destino = input('Moeda destino: ')

def leiafloat():
    while True:
        try:
            n = float(input('Valor: '))
            return n
        except:
            print('Por favor, digita um valor válido.')

def leiaint():
    while True:
        try:
            n = int(input('Digita uma opção: '))
            if n not in [1, 2, 3, 4]: continue
            return n
        except:
            print('Digita uma opção válida.')

def ler_opc():
    while True:
        try:
            n = int(input('Quer continuar (1.sim, 2.não)? '))
            if n not in [1, 2]: continue
            return n
        except:
            print('Digita uma opção válida.')

while True:
    print('=' * 30)
    print('Conversor de moedas'.center(30))
    print('=' * 30)
    valor = leiafloat()
    print('=' * 30)
    print("""Moeda origem:
[1] - BRL
[2] - USD
[3] - EUR
[4] - Outro""")
    opc = leiaint()
    if opc == 1: 
        moeda_origem = 'BRL'
    elif opc ==2:
        moeda_origem = 'USD'
    elif opc ==3:
        moeda_origem = 'EUR'
    else:
        moeda_origem = input('Informe uma moeda origem: ').strip()[:2]
    print('=' * 30)
    print("""Moeda destino:
[1] - BRL
[2] - USD
[3] - EUR
[4] - Outro""")
    opc = leiaint()
    if opc == 1: 
        moeda_destino = 'BRL'
    elif opc == 2:
        moeda_destino = 'USD'
    elif opc == 3:
        moeda_destino = 'EUR'
    else:
        moeda_destino = input('Informe uma moeda destino: ').strip()[:2]

    moeda_convertida = converter(valor, moeda_origem, moeda_destino)
    print(f'Moeda convertida de {valor} {moeda_origem} para {moeda_convertida:.2f} {moeda_destino}')
    
    if ler_opc() == 2: break
    limpar_terminal()