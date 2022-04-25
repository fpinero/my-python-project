my_set = {"Enero", "Febrero", "Marzo"}
# listar los elementos de un set
print("listando elementos del set")
for element in my_set:
    print(element)

print(f"\nañadiendo Abril al set")
my_set.add("Abril")

print("listando elementos del set tras añadir Abril")
for element in my_set:
    print(element)

print(f"\nEliminando Febrero del set")
my_set.remove("Febrero")

print("listando elementos del set tras eliminar Febrero")
for element in my_set:
    print(element)