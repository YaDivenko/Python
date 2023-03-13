#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с 
#номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме 
#последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
#Вам требуется написать программу, которая проверяет счастливость билета.

#*Пример:*

#385916 -> yes
#123456 -> no

n = int(input('Введите номер билетика из 6 цифр: '))

sum1 = n//100000+n//10000%10+n//1000%10
sum2 = n//100%10+n//10%10+n%10
res = 'yes' if sum1==sum2 else 'no'
print(res)