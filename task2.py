def ins_sort(array: list) -> list:
    """
    :param array: Список для сортировки (сортировка производится по числовому значению 2 элемента
    :return: Отсортированный по числовому значению 2 элемента список
    """
    N = len(array)
    for i in range(N):
        for j in range(i, 0, -1):
            num1 = array[j][1].index('-')
            num2 = array[j - 1][1].index('-')
            if int(array[j][1][:num1]) < int(array[j - 1][1][:num2]):
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
    return array


austronaut_time = open('astronaut_time.txt',
                       encoding='utf-8').read().splitlines()  # Создаём переменную для чтения таблицы
austronaut_time = austronaut_time[1:]  # Убираем первую строку с заголовками
for i in range(len(austronaut_time)):  # Проходимся по списку
    austronaut_time[i] = austronaut_time[i].split('>')  # Разбиваем строку на значения
sorted_austronaut_time = ins_sort(austronaut_time)  # Создаём отсортированную копию списка
actual_austronaut_times = []  # Создаём список для определения актуального времени в каютах
for temp in austronaut_time:  # Проходимя по таблице
    time = [num for num in temp[-2].split(':')]  # Получаем значения часов, минут и секунд в строковом виде
    hour = int(time[0])  # Переводим значения часов в целочисленный тип
    if hour + int(temp[-1]) >= 10:  # Формируем актуальное время
        actual_austronaut_times.append(('0' if (temp_time := (
                int(temp[-1]) + int(time[0]))) % 24 < 10 else '') + f'{temp_time % 24}:{time[1]}:{time[2]}')
    else:
        actual_austronaut_times.append(
            ('0' if (temp_time := (int(temp[-1]) + int(time[0]))) % 24 < 10 else '') +
            f'{temp_time % 24}:{time[1]}:{time[2]}')  # Добавляем актуальное время в список
for i in range(3):
    print(
        f'На станции {sorted_austronaut_time[i][1]} в каюте {sorted_austronaut_time[i][2]} восстановлено время.'
        f' Актуальное время: {actual_austronaut_times[i]}')  # Выводим результат
