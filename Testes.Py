from Automacao import iniciar_navegador, acessar_speedtest, obter_dados, fechar_navegador
from Processamento import processar_dados
from Planilha import obter_mes_atual, carregar_ou_criar_planilha, salvar_dados

# Caminho para o arquivo Excel
caminho_arquivo = 'C:/Users/rNz/Desktop/Monitoramento de Link.xlsx'

# Inicia o navegador e acessa o Speedtest
navegador = iniciar_navegador()
acessar_speedtest(navegador)

# Obtém os dados
Data, Hora, Download, Upload, Min, Max, Media = obter_dados(navegador)

# Processa os dados
Download, Upload, Min, Max, Media = processar_dados(Download, Upload, Min, Max, Media)

# Obtém o mês atual para a planilha
MesPlanilha = obter_mes_atual()

# Carrega ou cria a planilha
plan, pag_med = carregar_ou_criar_planilha(caminho_arquivo, MesPlanilha)

# Salva os dados na planilha
salvar_dados(plan, pag_med, Data, Hora, Download, Upload, Min, Max, Media, caminho_arquivo)

# Fecha o navegador
fechar_navegador(navegador)
