from forex_python.converter import CurrencyRates

def converter_moeda(valor, moeda_origem, moeda_destino):
    c = CurrencyRates()
    taxa = c.get_rate(moeda_origem, moeda_destino)
    valor_convertido = valor * taxa
    return valor_convertido

# Exemplo de uso:
valor_em_usd = 1
moeda_convertida = converter_moeda(valor_em_usd, 'USD', 'BRL')
print(f'{valor_em_usd} USD é igual a {moeda_convertida:.2f} BRL')
