# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4


def sum_ab(a, b):
    if a == 0:
        return b
    return sum_ab(a-1, b+1)


a = int(input("Введите неотрицительное число "))
b = int(input("Введите неотрицательно число "))
print(sum_ab(a, b))