import datetime

user_input = input("Enter your goal with a deadline separated by colon (ej. Aprender Python:30.07.2022)\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

datetime_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
# calculate how many days now till deadline
today = datetime.datetime.today() # asigna a today la fecha actual

time_till = (datetime_date - today)
if time_till.days < 0:
    min_fecha = str(datetime.date.today()).split("-")
    # print(f"min_fecha= {min_fecha}")
    min_fecha_formateada = min_fecha[2] + "." + min_fecha[1] + "." + min_fecha[0]
    # print(f"min_fecha_formateada= {min_fecha_formateada}")
    print(f"Indica una fecha posterior a hoy {min_fecha_formateada}")
else:
    final_msg = f"Dear User! Time remaining to your goal: {goal} are {time_till.days} days"
    print(final_msg)

