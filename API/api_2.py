import requests
import json


# url = 'https://jsonplaceholder.typicode.com/photos'
# response = requests.get(url)
# if response.status_code == 200:
#     data = response.json()[:10]
#     print(data)
# else:
#     print("Error al obtener los datos. Código de estado:", response.status_code)


#TIPOS DE PETICIONES HTTP
#GET: OBTENER DATOS
#POST: CREAR DATOS  
#PUT: ACTUALIZAR DATOS
#DELETE: ELIMINAR DATOS
#PATCH: ACTUALIZAR PARCIALMENTE DATOS

#HEAD: OBTENER CABECERAS
#OPTIONS: OBTENER LOS METODOS HTTP SOPORTADOS POR UN SERVIDOR
#TRACE: PERMITE VER LA RUTA QUE SIGUE UNA PETICION
#CONNECT: CONECTAR CON EL SERVIDOR


#POST
url = 'https://jsonplaceholder.typicode.com/posts'
payload = {
    'title': 'foo',
    'body': 'este es nuestro primer post',
    'userId': 1
}
headers = {
    'Content-Type': 'application/json'
}
response = requests.post(url, data=json.dumps(payload), headers=headers)
print(response.text)


#GET DE NUESTRO RECURSO
# url = 'https://jsonplaceholder.typicode.com/posts'
# response = requests.get(url)
# data = json.loads(response.text)
