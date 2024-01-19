from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd 
import requests

# ANO DA TEMPORADA QUE SERÁ ANALISADA
year = 2023

# URL DA PÁGINA PARA COLETA DOS DADOS
url_nba = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)

# CRIANDO A VARIÁVEL PAGE E UTILIZANDO O MÉTODO REQUESTS PARA COLETA DOS DADOS
page = requests.get(url_nba)

# VISUALIZANDO A PERMISSÃO DA URL PARA COLETA DE DADOS
print(page)

# CRIANDO VARIÁVEIS PARA ATRIBUIREM A URL PARA COLETA E EXTRAÇÃO DOS DADOS
html_nba = urlopen(url_nba)
soup_nba = BeautifulSoup(html_nba, features="html.parser")

