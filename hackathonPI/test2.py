import requests
from bs4 import BeautifulSoup


servicosStatus = {
        "Visualizando conteudo": "",
        "Criar e editar":"",
        "Autenticacao e gerenciamento de usuarios":"",
        "Procurar":"",
        "Notificacoes":"",
        "Administracao":"",
        "Mercado":"",
        "Movel":"",
        "Compra e Licenciamento":"",
        "Inscrever-se":"",
        "Automação para Jira":""
        }

link = "https://ocistatus.oraclecloud.com/#/"

requisicao = requests.get(link)

print(requisicao)

site = BeautifulSoup(requisicao.text, "html.parser")

print(site.prettify())

statusRaiz = site.find("th", "category")

print(statusRaiz)

#statusOperacao = statusRaiz["alt"]

#print(statusOperacao)

#     for p in range(11):

#         statusRaizStr = str(statusRaiz[p])

#         open = False

        
#         if(status == 'Operational'):
#             respost = True
#         else:
#             respost = False

#         for v in servicosStatus:
#             servicosStatus[v] = respost

#     return servicosStatus

# def lerDicionario(dicionario):
#     acumula = ''
#     for k, v in dicionario.items():
#         acumula += str(f"\nServiço: {k}  -  Status: {v} ")
#     return acumula


# #print(servicosStatus[Visualizando conteudo])

# statusServicosJira = statusJira()
# print(lerDicionario(statusServicosJira))