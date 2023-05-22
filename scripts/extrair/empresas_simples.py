import git
import requests

csv_url= "https://raw.githubusercontent.com/TesteBINeoway/testeAnalistaBI/main/an_bi/spreadsheets/empresas_simples.csv"
resp = requests.get(csv_url)

with open ("empresas_simples.csv",'wb') as file:
    file.write(resp.content)
    print('Download concluído!')