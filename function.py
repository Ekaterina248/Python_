# Задача
# Необходимо создать функцию sumNumbers(n), которая будет
# считать сумму всех элементов от 1 до n.
def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(summa)
sumNumbers(5)
print('-----------------------------')
def sumNumbers1(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa
s=sumNumbers1(5)
print(s)
print('-----------------------------')
def sumNumbers3(n, y='hellow'):   #hellow   #y- вывели на печать
    print(y)                      #15       #в s  записали точто в return
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa
s=sumNumbers3(5)
print(s)
print('-----------------------------')
def sumNumbers4(n, y='hellow'):   # y= 'hellow' по умолчанию, если при вызове функции не будет задано другое условие
    print(y)                      
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa
s=sumNumbers3(5,'zamena y')        # zamena y  #y- переприсвоили и вывели на печать     
print(s)                           # 15        #в s  записали точто в return
print('Задача2----------------------------')
def sum_str(*args):    # * функция, которая принимает неограниченное кол-во аргументов
    res=''
    for i in args:
        res +=str(i)
    return res
print(sum_str('c','a','t'))
print(sum_str('c','a','t',' ','d','o','g'))
print(sum_str(1,8,9,10))
print('-----------------------------')
s='Hellow'+' World'
print(s)
print('МОДУЛИ-------------------------')
import modul1 as m1 # импортируем файл, в котором прописаны функции
print(m1.max1(4,5))  # обращаемся к функции : имя файла.имя функции(аргументы)
# from modul1 import *
# print(max1(4,5))
print('функция пример-------------------------')
def new_string(n, count=3):
    return n * count
print(new_string('2'))
print(new_string('2',5))
print('РЕКУРСИЯ-------------------------')
# задачу: Пользователь вводит число n. Необходимо вывести n - первых
# членов последовательности Фибоначчи
print('ФИБОНАЧИ')
def fib(n):
    if n in [1, 2]: # базис. условие выхода
        return 1
    return fib(n - 1) + fib(n - 2)
n=10
list_1 = []
for i in range(1, n+1):
    list_1.append(fib(i))
print(list_1)