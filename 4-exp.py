sum_input = input("Введите сумму: ")

# Убедимся, что входная строка содержит "руб"
if "руб" not in sum_input:
    print("Некорректный формат суммы")
else:
    parts = sum_input.split()

    # Проверим наличие индексов и корректность данных
    if len(parts) >= 2 and 'руб' in parts:
        rub_index = parts.index('руб')

        # Попробуем преобразовать рубли в число
        if rub_index > 0 and parts[rub_index - 1].isdigit():
            rub = int(parts[rub_index - 1])
        else:
            print("Некорректный формат суммы")
            exit()

        # Проверяем наличие копеек и их правильность
        if 'коп' in parts:
            kop_index = parts.index('коп')
            if kop_index > rub_index and parts[kop_index - 1].isdigit():
                kop = int(parts[kop_index - 1])
            else:
                print("Некорректный формат суммы")
                exit()
        else:
            kop = 0

        # Проверка на корректность копеек
        if 0 <= kop <= 99:
            print(f"{rub}.{kop:02} ₽")
        else:
            print("Некорректный формат суммы")
    else:
        print("Некорректный формат суммы")