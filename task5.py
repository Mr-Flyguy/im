austronaut_time = open('astronaut_time.txt',
                       encoding='utf-8').read().splitlines()  # Создаём переменную для чтения таблицы
hash = dict()  # Создаём хэш-таблицу
for i in austronaut_time[1:]:  # Проходим по списку
    temp = i.split('>')  # Разбиваем строку на элементы
    hash[temp[2]] = {'Номер часов': temp[0], 'Номер станции': temp[1], 'Время остановки часов': temp[3],
                     'Кол-во часов простоя': temp[4]}  # Формируем элемент хэш-таюдицы
for i in range(10):
    print(f'Каюта - {austronaut_time[1:][i].split('>')[2]}, '
          f'информация - {hash[austronaut_time[1:][i].split('>')[2]]}')  # Выводим информацию о первых 10 каютах
