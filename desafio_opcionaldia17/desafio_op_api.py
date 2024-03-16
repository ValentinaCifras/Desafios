import requests
import json

url = "https://reqres.in/api/users"

#Requerimiento 1: obtener informacion de la api

def request_get(url):
  return json.loads(requests.get(url).text)


response = request_get("https://reqres.in/api/users")
users_data = response['data']
for user in users_data:
  print(user)
    








