import requests


url = "https://reqres.in/api/users/6"


#Requerimiento 4: eliminar un usuario
response = requests.request("DELETE", url)
delete = response


print(delete)
