import git
import requests

csv_url= "https://raw.githubusercontent.com/TesteBINeoway/testeAnalistaBI/main/an_bi/spreadsheets/cotacoes_bolsa.csv"
resp = requests.get(csv_url)

with open ("cotacoes_bolsa.csv",'wb') as file:
    file.write(resp.content)
    print('Download concluído!')