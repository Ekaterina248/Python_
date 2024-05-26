# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n (само число)
# Input: 5
# Output: yes
def prostoe_num(n):
    flag=True
    for i in range(2,n):
        if n%i==0:
            flag=False
            break
    if flag==True:
        print(f'{n} - Простое число')
    else:
        print(f'{n} - Составное число')

n1=int(input('Введите чило: '))
prostoe_num(n1)    

