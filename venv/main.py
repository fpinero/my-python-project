print("Hello World")
print("----_")
print(f"20 days are {20 * 24 * 60} minutes")
print("----_")
calculation_to_seconds = 24 * 60 * 60
calculation_to_minutes = 24 * 60
print(f"20 days are {20 * calculation_to_seconds} seconds (here I'm using a variable to compute the result)")
print("----_")


def days_to_minute():
    print(f"50 days are {50 * calculation_to_seconds} seconds (here I'm into a function compute the result)")


days_to_minute()
print("----_")


def days_to_minute_with_params(days):
    if days > 0:
        print(
            f"{days} days are {days * calculation_to_seconds} seconds (here I'm passing days as a param to a function "
            f"compute the result)")
    else:
        print(f"Invalid number {days}")


days_to_minute_with_params(80)
print("----_")
user_input = input("Indica el número de días a comvertir a segundos:\n")
if user_input.isdigit():  # comprobemos que el usuario ha introducido un número entero
    days_to_minute_with_params(int(user_input))  # los imputs siempre retornan Strings
else:
    print(f"Ha introducido un valor inválido")


def days_to_minute_with_params_with_return(days_to_calculate):
    try:  # por si el usuario indica un número tan alto que provoque un desborde de la pila
        if days_to_calculate > 0:
            return f"{days_to_calculate} days are {days_to_calculate * calculation_to_seconds} seconds (here I'm " \
                   f"returning the result from the function) "
        elif days_to_calculate == 0:
            return f"Invalid number, the number can not be zero {days_to_calculate}"
        else:
            return f"Invalid number, the number is negative {days_to_calculate}"
    except ValueError:
        return f"No se pudo calcular el valor introducido {days_to_calculate}"


print("----_")
user_input2 = ""
while user_input2 != "q":
    user_input2 = input("Indica el número de días a comvertir a segundos (q=exit):\n")
    if user_input2 != "q":
        if user_input2.isdigit():  # comprobemos que el usuario ha introducido un número entero
            segundos_recividos = days_to_minute_with_params_with_return(int(user_input2))
            print(segundos_recividos)
        else:
            print(f"Ha introducido un valor inválido")

print("----_")
user_input3 = ""
while user_input3 != "q":
    user_input3 = input("Indica una lista de números separados por comas a comvertir a segundos (q=exit):\n")
    if user_input3 != "q":
        for num_of_days_element in user_input3.split(","):
            if num_of_days_element.isdigit():  # comprobemos que el usuario ha introducido un número entero
                segundos_recividos = days_to_minute_with_params_with_return(int(num_of_days_element))
                print(segundos_recividos)
            else:
                print(f"Ha introducido el valor inválido: {num_of_days_element}, se ignora")

print("----_")
user_input4 = ""
while user_input4 != "q":
    user_input4 = input("Indica una lista de números (se mostrará una sóla vez los valores duplicados) separados por "
                        "comas a "
                        "comvertir a segundos (q=exit):\n")
    if user_input4 != "q":
        for num_of_days_element in set(user_input4.split(",")):  # set elimina los valores duplicados de una lista
            if num_of_days_element.isdigit():  # comprobemos que el usuario ha introducido un número entero
                segundos_recividos = days_to_minute_with_params_with_return(int(num_of_days_element))
                print(segundos_recividos)
            else:
                print(f"Ha introducido el valor inválido: {num_of_days_element}, se ignora")


def days_to_minute_with_params_with_dictionary(days_to_calculate, unit):
    try:  # por si el usuario indica un número tan alto que provoque un desborde de la pila
        if days_to_calculate > 0:
            if unit == "segundos":
                return f"{days_to_calculate} days are {days_to_calculate * calculation_to_seconds} seconds (here I'm " \
                       f"returning the result from the function using a dictionary) "
            elif unit == "minutos":
                return f"{days_to_calculate} days are {days_to_calculate * calculation_to_minutes} minutes (here I'm " \
                       f"returning the result from the function using a dictionary) "
        elif days_to_calculate == 0:
            return f"Invalid number, the number can not be zero {days_to_calculate}"
        else:
            return f"Invalid number, the number is negative {days_to_calculate}"
    except ValueError:
        return f"No se pudo calcular el valor introducido {days_to_calculate}"


print("----_")
user_input5 = ""
while user_input5 != "q":
    user_input5 = input("Indica un número y a lo que deseas convertirlos minutos o segundos (ej:50:minutos)"
                        "(q=exit):\n")
    if user_input5 != "q":
        days_and_unit = user_input5.split(":")
        days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
        print(days_to_minute_with_params_with_dictionary(int(days_and_unit_dictionary["days"]),
                                                         days_and_unit_dictionary["unit"]))
