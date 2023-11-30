import requests

class Subject:
    
    def __init__(self):
        #Cria uma lista de observadores
        self.observers = []
        self.status = "up"

    #Adiciona um observador a lista de observadores
    def attach(self, observer):
        self.observers.append(observer)

    #Remove um observador
    def detach(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

class Server:
    def __init__(self, nome, url):
        self.nome = nome
        self.url = url
        self.status = "up"

    #Verifica se o status da requisição é diferente de 200 (Caiu)
    def check_status(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            self.status = "down"
    
    #Altera o status
    def update(self, subject):
        if subject.status == "down":
            print(f"O servidor {subject.nome} está indisponível.")
            
class Observer:
    def update(self, subject):
        pass

class ServerObserver(Observer):
    def __init__(self, nome):
        self.nome = nome

    def update(self, subject):
        if subject.status == "down":
            print(f"O servidor {subject.nome} está indisponível.")


if __name__ == "__main__":
    subject = Subject()  # Cria uma instância da classe Subject

    server1 = Server("AWS", "https://health.aws.amazon.com/health/status")
    server2 = Server("JIRA", "https://jira-software.status.atlassian.com/")
    server3 = Server("ORACLE", "https://ocistatus.oraclecloud.com/#/JIRO")

    observer1 = ServerObserver("AWS")
    observer2 = ServerObserver("JIRA")
    observer3 = ServerObserver("ORACLE")

    subject.attach(observer1)  # Anexa os observadores à instância Subject
    subject.attach(observer2)
    subject.attach(observer3)

    for _ in range(10):
        server1.check_status()
        server2.check_status()
        server3.check_status()

        subject.notify_observers()  # Notifica os observadores por meio da instância Subject
