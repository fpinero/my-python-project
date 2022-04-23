print("Hello World")
print("----_")
print(f"20 days are {20 * 24 * 60} minutes")
print("----_")
calculation_to_seconds = 24 * 60 * 60
print(f"20 days are {20 * calculation_to_seconds} seconds (here I'm using a variable to compute the result)")
print("----_")


def days_to_minute():
    print(f"50 days are {50 * calculation_to_seconds} seconds (here I'm into a function compute the result)")


days_to_minute()
print("----_")


def days_to_minute_with_params(days):
    print(f"{days} days are {days * calculation_to_seconds} seconds (here I'm passing days as a param to a function "
          f"compute the result)")


days_to_minute_with_params(80)
print("----_")
user_input = input("Indica el número de días a comvertir a segundos:\n")
days_to_minute_with_params(int(user_input))  # los imputs siempre retornan Strings


def days_to_minute_with_params_with_return(days):
    return f"{days} days are {days * calculation_to_seconds} seconds (here I'm retuning the result)"


print("----_")
user_input2 = input("Indica el número de días a comvertir a segundos:\n")
segundos_recividos = days_to_minute_with_params_with_return(int(user_input))
print(segundos_recividos)
