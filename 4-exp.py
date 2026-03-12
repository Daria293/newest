sum_input = input("Введите сумму: ")
ignore = sum_input.lower()
ignore2 = ignore.split(".")
rub, kop = ignore2

if len(kop) > 2:
    print("Некорректный формат суммы")
else:
    formatted_sum = f"{rub}.{kop:0<2}₽"
    print(formatted_sum)
