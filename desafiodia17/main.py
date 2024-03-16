from string import Template
from funciones import request_get
import json

url = "https://aves.ninjas.cl/api/birds"

#llamar a la api para obtener informacion
response = request_get(url)

lista_url= [(elemento['name']['spanish'], elemento['name'] ['english'], elemento['images']['main']) for elemento in response]
#print(lista_url)

nuevo_card =  """<div class="col-sm-12 col-md-6 col-lg-4 col-xl-4 p-3">
                    <div class="card" style="width: 18rem;">
                        <img src="$url" class="card-img-top" alt="...">
                        <div class="card-body">
                        <h4 class="card-title text-center">$spa</h4>
                        <p class="card-text text-center fs-5">$eng</p>
                        </div>
                    </div>
                </div>"""

img_template = Template(nuevo_card)
texto_img =''

for spanish, english, image_url in lista_url:
    texto_img += img_template.substitute(spa=spanish, eng=english, url=image_url) + '\n'


html_template = Template ('''<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Aves de Chile</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body class=bg-dark>
    <h1 class="text-center text-secondary fw-semibold p-4">Aves de Chile</h1>
    <div class="container">
        <div class="row">
            $body
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>
''')

html = html_template.substitute(body = texto_img)
#print(html)

archivo = open('index.html','w+', encoding='utf-8')
archivo.write(html)
archivo.close()
