import global_vars

def days_to_minute_with_params_with_dictionary(days_to_calculate, unit):
    try:  # por si el usuario indica un número tan alto que provoque un desborde de la pila
        if days_to_calculate > 0:
            if unit == "segundos":
                return f"{days_to_calculate} days are {days_to_calculate * global_vars.calculation_to_seconds} seconds (here I'm " \
                       f"returning the result from the function using a dictionary) "
            elif unit == "minutos":
                return f"{days_to_calculate} days are {days_to_calculate * global_vars.calculation_to_minutes} minutes (here I'm " \
                       f"returning the result from the function using a dictionary) "
            else:
                return f"unsupported unit {unit}"
        elif days_to_calculate == 0:
            return f"Invalid number, the number can not be zero {days_to_calculate}"
        else:
            return f"Invalid number, the number is negative {days_to_calculate}"
    except ValueError:
        return f"No se pudo calcular el valor introducido {days_to_calculate}"