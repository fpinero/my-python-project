from user import *   # importar con este formato evita tener que poner el nombre del fichero importado delaante de cada método de la clase

app_user_one = User("email@email.com", "Lorenzo Lamas", "pwd123", "Rey de las camas")
app_user_one.get_user_info()
print("\ncambiando el job tittle del usuario creado\n")
app_user_one.change_job_tittle("Presidente de Colchonetas, SA")
app_user_one.get_user_info()