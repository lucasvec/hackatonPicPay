
#=========================================== JIRA ===============================================
#URl da aba de servidores do JIRA
url = "https://jira-software.status.atlassian.com/" #URl válida
response = requests.get(url)
status = ""

#Verifica se a aba de servidores do JIRA está em pé
if response.status_code == 200:
    status += "\nAba de servidores do JIRA está de pé!"

else:
    status += "\nA aba de servidores do JIRA caiu."



#=========================================== ORACLE ==============================================
#URl da aba de servidores do ORACLE
url = "https://ocistatus.oraclecloud.com/#/JIRO" #URl válida
response = requests.get(url)

#Verifica se a aba de servidores do ORACLE está em pé
if response.status_code == 200:
    status += "\nAba de servidores do ORACLE está de pé!"

else:
    status += "\nA aba de servidores do ORACLE caiu."



#=========================================== AWS =================================================
#URl da aba de servidores do AWS
url = "https://health.aws.amazon.com/health/status" #URl válida
response = requests.get(url)

#Verifica se a aba de servidores do AWS está em pé
if response.status_code == 200:
    status += "\nAba de servidores do AWS está de pé!"

else:
    status += "\nA aba de servidores do AWS caiu."
    
print(status)

# open = False

# acumula = ''

# print(requisicao)

# for i in requisicao:
#     if (i == '['):
#         open = True
#     else:
#         if(i == ']'):
#                 open = False;    
#         else:
#             if(open == True):
#                 acumula += i
    
#     print(i)
        
# print(acumula)        

    
# Teste Encontra Sao Paulo
# for p in (requisicao):
#     if (p == 'Sao Paulo'):
#         print(p)
#     elif (p == 'src="/static/media/success.12ad79f1.svg"'):
#         print(p)



