import git
import requests

csv_url= "https://raw.githubusercontent.com/TesteBINeoway/testeAnalistaBI/main/an_bi/spreadsheets/empresas_nivel_atividade.csv"
resp = requests.get(csv_url)

with open ("empresas_nivel_atividade.csv",'wb') as file:
    file.write(resp.content)
    print('Download concluído!')