import requests
from bs4 import BeautifulSoup

def statusJira():
    
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

    link = "https://jira-software.status.atlassian.com/"

    requisicao = requests.get(link)

    site = BeautifulSoup(requisicao.text, "html.parser")

    statusRaiz = site.find_all(class_="component-status")

    for p in range(11):

        statusRaizStr = str(statusRaiz[p])

        open = False

        status = ''

        for i in statusRaizStr:
            if(i == '>'):
                open = True
            else:
                if(i == '<'):
                    open = False
                else:
                    if(open == True):
                        status += i

        status = status.strip()

        if(status == 'Operational'):
            respost = True
        else:
            respost = False

        for v in servicosStatus:
            servicosStatus[v] = respost

    return servicosStatus

def lerDicionario(dicionario):
    acumula = ''
    for k, v in dicionario.items():
        acumula += str(f"\nServiço: {k}  -  Status: {v} ")
    return acumula


#print(servicosStatus[Visualizando conteudo])

statusServicosJira = statusJira()
print(lerDicionario(statusServicosJira))









