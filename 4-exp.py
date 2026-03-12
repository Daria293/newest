sum_input = input("Введите сумму: ").lower()  # Приводим строку к нижнему регистру

# Убедимся, что входная строка содержит "руб"
if "руб" not in sum_input:
    print("Некорректный формат суммы")
else:
    parts = sum_input.split()

    rub = None
    kop = 0  # По умолчанию копейки равны 0

    for i, part in enumerate(parts):
        if part `==` 'руб' and i > 0 and parts[i - 1].isdigit():
            rub = int(parts[i - 1])
        elif part `==` 'коп' and i > 0 and parts[i - 1].isdigit():
            kop = int(parts[i - 1])

    # Проверка, что нашли хотя бы количество рублей
    if rub is not None:
        if 0 <= kop <= 99:
            print(f"{rub}.{kop:02} ₽")
        else:
            print("Некорректный формат суммы")
    else:
        print("Некорректный формат суммы")