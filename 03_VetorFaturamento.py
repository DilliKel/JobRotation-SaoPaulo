import xml.etree.ElementTree as ET

# Lê o arquivo XML
tree = ET.parse('dados.xml')
root = tree.getroot()

# Extrai os valores de faturamento
faturamento = []
for row in root.findall('row'):
    dia = int(row.find('dia').text)
    valor = float(row.find('valor').text)
    faturamento.append(valor)

# Calcula o menor e o maior valor de faturamento
menor_valor = min(faturamento)
maior_valor = max(faturamento)

# Calcula a média mensal
media_mensal = sum(faturamento) / len(faturamento)

# Calcula o número de dias em que o faturamento foi superior à média mensal
dias_acima_da_media = len([valor for valor in faturamento if valor > media_mensal])

# Imprime os resultados
print(f'Menor valor de faturamento: {menor_valor:.2f}')
print(f'Maior valor de faturamento: {maior_valor:.2f}')
print(f'Número de dias com faturamento acima da média mensal: {dias_acima_da_media}')
