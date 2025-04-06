def converter_para_float(valor):
    try:
        return float(valor.replace(' Mbps', '').replace(',', '.'))
    except ValueError:
        return 0.0

def processar_dados(Download, Upload, Min, Max, Media):
    # Processa os valores, removendo unidades e convertendo para float ou int
    Download = converter_para_float(Download)
    Upload = converter_para_float(Upload)
    
    return Download, Upload, Min, Max, Media
