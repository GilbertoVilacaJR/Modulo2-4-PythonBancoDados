import requests
import json

def buscar_dados():
    request=requests.get('http://3e7a-179-73-200-33.sa.ngrok.io/eventoapi/eventos/')
    dados=json.loads(request.content)
    print(dados)
    print()

def add():
    url='http://3e7a-179-73-200-33.sa.ngrok.io/eventoapi/eventos/'
    play={
        'nome': 'teste X', 
        'description': 'teste11,1', 
        'telefone': '(81) 98882-2222', 
        'email': 'teste@hotmail.com', 
        'data_nascimento': '1983-03-23', 
        'user': 2
        }
    request=requests.post(url, data=play)
    print('foi')

def deletar_dados(id):
    request=requests.delete('http://3e7a-179-73-200-33.sa.ngrok.io/eventoapi/eventos/1/')
    print("Ok")


buscar_dados()
#add()
#deletar_dados(1)