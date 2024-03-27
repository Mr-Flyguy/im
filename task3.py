austronaut_time = open('astronaut_time.txt',
                       encoding='utf-8').read().splitlines()  # Создаём переменную для чтения таблицы
while True:
    cabinNumber = input('Введите номер кабины: ')  # Запрашиваем номер каюты
    if cabinNumber == 'none':  # Проверяем на команду завершения программы
        break
    for i in austronaut_time[1:]:  # Проходим по списку для поиска
        temp = i.split('>')  # Разбиваем строку на элементы
        if temp[2] == cabinNumber:  # Проверяем, нужна ли это каюта
            time = [num for num in temp[-2].split(':')]  # Получаем строковые значения времени
            hour = int(time[0])  # Получаем целочисленное значение часов
            if hour + int(temp[-1]) >= 10:  # Формируем строку с актуальным временем
                temp[-1] = ('0' if (temp_time := (
                        int(temp[-1]) + int(time[0]))) % 24 < 10 else '') + f'{temp_time % 24}:{time[1]}:{time[2]}'
            else:
                temp[-1] = ('0' if (temp_time := (
                            int(temp[-1]) + int(time[0]))) % 24 < 10 else '') + f'{temp_time % 24}:{time[1]}:{time[2]}'
            print(
                f'В каюте {cabinNumber} восстановлено время (время остановки: {temp[-2]}).'
                f' Актуальное время: {temp[-1]}')  # Выводим результат
            break  # Завершаем поиск
    else:
        print('В этой каюте всё хорошо')  # Вывод, если каюта не найдена
