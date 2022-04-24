my_list = ["Enero", "Febrero", "Marzo"]
print(f"imprimiendo el segundo elemento de la lista:")
print(my_list[1])
print("-----")


def recorre_lista():
    print("recorriendo toda la lista e imprimiendo sus elementos")
    for items_in_my_list in my_list:
        print(items_in_my_list)
    print("-----")


recorre_lista()
print("Añadiendo un mes más a la lista")
my_list.append("Abril")
recorre_lista()


