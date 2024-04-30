import requests
import json
from string import Template

def get_url(url):
    return json.loads(requests.get(url).text)
    
data = get_url('https://jsonplaceholder.typicode.com/photos')[:5]
# print(len(data))

print(data[0].keys())
# print(data[0].values())

img_template = Template('<img src="$url"')
print(img_template)
# imagen = img_template.substitute(url = 'hola')
#print(imagen)


html_template = Template('''<!DOCTYPE html>
<html>
    <head>
        <title>Título de la Página</title>
    </head>
    <body>
        <h1>Nuestra página Web</h1>
        $body
    </body>
</html>
''')

lista_url = [elemento['url'] for elemento in data]
texto_img = ''
for url in lista_url:
    print(url)  
    texto_img += img_template.substitute(url = url)+'\n'



