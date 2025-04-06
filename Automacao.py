from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

def iniciar_navegador():
    servico = Service(GeckoDriverManager().install())
    navegador = webdriver.Firefox(service=servico)
    return navegador

def acessar_speedtest(navegador):
    navegador.get('https://www.speedtest.net/pt')
    WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[1]/a/span[4]')))
    navegador.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[1]/a/span[4]').click()
    time.sleep(40)  # Espera até o teste ser concluído

def obter_dados(navegador):
    Data = datetime.today().strftime('%Y-%m-%d')
    Hora = datetime.now().time().strftime('%H:%M:%S')

    Download = navegador.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
    Upload = navegador.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
    Min = int(navegador.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[3]/div/div[3]/div/div/div[2]/div[2]/div/span[3]/span').text)
    Max = int(navegador.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[3]/div/div[3]/div/div/div[2]/div[2]/div/span[4]/span').text)
    Media = int(navegador.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[3]/div/div[3]/div/div/div[2]/div[2]/div/span[2]/span').text)

    return Data, Hora, Download, Upload, Min, Max, Media

def fechar_navegador(navegador):
    navegador.quit()
