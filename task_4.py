'''
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
'''

s = int(input('Введите количество журавликов: '))

n=s//(1+4+1)
m=(2+2)*s//(1+4+1)

print (f'Сережа сделал {n} журавлика(ов)')
print (f'Катя сделала {m} журавлика(ов)')
print (f'Сережа сделал {n} журавлика(ов)')