austronaut_time = open('astronaut_time.txt',
                       encoding='utf-8').read().splitlines()  # Создаём переменную для чтения таблицы
new_time = open('new_time.csv', 'w')  # Создаём переменную для записи в новую таблицу
new_time.write(austronaut_time[0].replace('>', ',') + '\n')  # Добавляем в таблицу строку-заголовок
for i in austronaut_time[1:]:  # Проходимя по таблице
    temp = i.split('>')  # Разбиваем строку на элементы
    time = [num for num in temp[-2].split(':')]  # Получаем значения часов, минут и секунд в строковом виде
    hour = int(time[0])  # Переводим значения часов в целочисленный тип
    if hour + int(temp[-1]) >= 10:  # Формируем актуальное время
        temp[-1] = ('0' if (temp_time := (int(temp[-1]) + int(
            time[0])) % 24) < 10 else '') + f'{temp_time%24}:{time[1]}:{time[2]}'
    else:
        temp[-1] = ('0' if (temp_time :=(int(temp[-1]) + int(
            time[0]))) % 24 < 10 else '') + f'{temp_time%24}:{time[1]}:{time[2]}'
    if temp[2] == '98-OYE':  # Ищем актуальное время для заданной каюты
        print(f'{temp[-1]} - действительное время для каюты: {temp[2]}')
    new_time.write(','.join(temp) + '\n')  # Записываем измененную строку в новую таблицу
