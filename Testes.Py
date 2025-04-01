import datetime

# Lista de meses em português
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Captura o número do mês atual (1-12)
mes_numero = datetime.datetime.now().month

# Obtém o nome do mês, com a primeira letra maiúscula
mes_atual = meses[mes_numero - 1]

print(mes_atual)