from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd 
import requests
from datetime import date

# INFORMANDO OS ANOS DESEJADOS PARA EXTRAÇÃO DOS DADOS
start = date(2018, 1, 1)
end = date(2022, 1, 1)

# CRIANDO UM LOOP FOR PARA PEGAR A SEQUÊNCIAS DOS ANOS DESEJADOS PARA COLETA DOS DADOS
year_range = [year for year in range(start.year, end.year)]
print(year_range)




