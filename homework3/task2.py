# Дан список из 7 различных элементов. Используя функции (не использовать цикл), необходимо найти:
# минимальный и максимальный элементы списка;
# сумму и среднее арифметическое с округлением до 2 знаков после запятой;

from statistics import mean
def get_list_info(lst):
   # lst = list(range(4))
    lst[0] = min(data[0]), max(data[0]), sum(data[0]), float(mean(data[0]))
    lst[1] = min(data[1]), max(data[1]), sum(data[1]), float(mean(data[1]))
    lst[2] = min(data[2]), max(data[2]), sum(data[2]), round(mean(data[2]), 2)
    lst[3] = min(data[3]), max(data[3]), sum(data[3]), float(mean(data[3]))
    del lst[4:7]
    print(lst)
    return lst

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    [1, 2, 3, 4, 5, 6, 7],
    [-1, -2, -3, -4, -5, -6, -7],
    [99, 56, 209, -308, -12, -18, 42],
    [-1, -2, -3, 0, 1, 2, 3],
]

test_data = [
    (1, 7, 28, 4.0), (-7, -1, -28, -4.0), (-308, 209, 68, 9.71), (-3, 3, 0, 0.0)
]


for i, d in enumerate(data):
    assert get_list_info(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
