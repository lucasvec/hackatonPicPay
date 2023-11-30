import requests
from bs4 import BeautifulSoup
from ast import literal_eval

#link = "https://health.aws.amazon.com/health/status"

link = "https://di1pzre3hzbi4.cloudfront.net/"
 
requisicao = requests.get(link)
 
site = BeautifulSoup(requisicao.text, "html.parser")

dicionario = str(site)

dic = literal_eval(site) 

for i in dic:
    for k, v in dic.items():
        print(f"\n{k} {v}")

