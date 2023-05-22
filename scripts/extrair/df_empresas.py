import git
import requests

csv_url= "https://raw.githubusercontent.com/TesteBINeoway/testeAnalistaBI/main/an_bi/spreadsheets/df_empresas.csv"
resp = requests.get(csv_url)

with open ("df_empresas.csv",'wb') as file:
    file.write(resp.content)
    print('Download concluído!')