from selenium import webdriver # primeira linha para importar o webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
import time    
from openpyxl import Workbook
import openpyxl as opx
 
servico = Service(GeckoDriverManager().install()) 
navegador = webdriver.Firefox(service=servico)


Meses = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
NMesAtual = datetime.now().month
MesPlanilha = Meses[NMesAtual]