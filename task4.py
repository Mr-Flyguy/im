austronaut_time = open('astronaut_time.txt',
                       encoding='utf-8').read().splitlines()  # Создаём переменную для чтения таблицы
first_half = []  # Создаём список с каютами, в которых время остановилось в первой половине дня
second_half = []  # Создаём список с каютами, в которых время остановилось во второй половине дня
for i in austronaut_time[1:]:  # Проходим по списку
    temp = i.split('>')  # Разбиваем строку на элементы
    time = [int(num) for num in temp[-2].split(':')]  # Получаем целочисленное значение времени
    if time[0] * 60 + time[1] > 12 * 60:  # Проверям, какая половина дня и добавляем в соответствующий список
        second_half.append(i)
    else:
        first_half.append(i)
print(f'{len(first_half)} станций остановилось с период с 00.00 до 12.00.')
print(f'{len(second_half)} станций остановилось с период с 12.01 до 23.59.')  # Выводим результаты
