import requests
import json

payload={}#data contenido que queremos pasar en la peticion
headers = {}#headers cabecera que queremos pasar en la peticion ejemplo token de autorizacion
url = "https://jsonplaceholder.typicode.com/posts"
# response = requests.get(url, headers=headers, data=payload)
# print(response.text)
# data = json.loads(response.text)
# print('userId:',data[0]['userId'])
# print('id:',data[0]['id'])
# print('title:',data[0]['title'])
# print('body:',data[0]['body'])

# print(data[0].keys())#['userId', 'id', 'title', 'body'] CLAVES
# print(data[0].values())#['userId', 'id', 'title', 'body'] VALORES
# # SI QUIERO MOSTRAR TODO LOS DATOS DE UNA SOLA VEZ
# for i in data:
#     print(i)
#     print('userId:',i['userId'])
#     print('id:',i['id'])
#     print('title:',i['title'])
#     print('body:',i['body'])
#     print('-----------------------------------')




#FUNCION DEL REQUESTS
def get_request(url):
    response = requests.get(url)
    data = json.loads(response.text)
    return data

data = get_request(url)
for i in data:
    print(i)
    print('userId:',i['userId'])
    print('id:',i['id'])
    print('title:',i['title'])
    print('body:',i['body'])
    print('-----------------------------------')



