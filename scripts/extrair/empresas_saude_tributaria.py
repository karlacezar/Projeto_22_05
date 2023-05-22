import git
import requests

csv_url= "https://raw.githubusercontent.com/TesteBINeoway/testeAnalistaBI/main/an_bi/spreadsheets/empresas_saude_tributaria.csv"
resp = requests.get(csv_url)

with open ("empresas_saude_tributaria.csv",'wb') as file:
    file.write(resp.content)
    print('Download concluído!')