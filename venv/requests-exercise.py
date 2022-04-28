import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
# print(response.text)
print(response.json())
print("mostrando el primer elemento del json recibido")
print(response.json()[0])
print("------------")
nana_projects = response.json()  # la respuesta es una lista que contiene un diccionario con el json

for project in nana_projects:  # se itera por la lista
    print(f"Project Name: {project['name']} \nProject Url: {project['web_url']}\n")  # se leen las keys del
    # diccionario que se desean
