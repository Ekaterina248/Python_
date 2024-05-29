def f(x):
    return x ** 2
g = f       # переменная g имеет ссылку на цукцию f
print(f(4)) # 16
print(g(4)) # 16
print("КАЛЬКУЛЯТОР========================")
def calc1(a,b):
    return a+b

def calc2(a,b):
    return a*b

def math(op, x, y):
    print(op (x, y))

math(calc2,5,2) 
math(calc1,5,2)

#////////////////////////////////////////////////////////////////////////////////////////
print("Lambda ФУНКЦИЯ========================")
calk1=lambda a,b: a+b
math(calc1,5,20)

math(lambda a,b: a+b,5,20)

print('ЗАДАЧА.1.-----------------------------')
# Задача для самостоятельного решения
# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]
data = [1, 2, 3, 5, 8, 15, 23, 38]
out = []
for i in data :
    if i % 2 == 0:
        out.append((i, i ** 2))
print(out)                       # [(2, 4), (8, 64), (38, 1444)]

print('ЗАДАЧА.1._Lambda Fuction-----------------------')
def select(f,col):              # функция создает новый список из элементов f(x), где х - принимает значение элементов списка col
    return[f(x) for x in col]   # см. Генератор списка.

def where(f,col):                    # Взвращаем список из элементов списка col, для которых верно условие, заданное функцией f(x)
    return[x for x in col if f(x) ]  # см. Генератор списка. 

rez=select(int,data)   # перевели в тип int все числа списка data
print(rez)                        # [1, 2, 3, 5, 8, 15, 23, 38]
rez=where(lambda x: x%2==0, rez)  # Взвращаем список из элементов списка rez, для которых lambda функция = true
print(rez)                        #[2, 8, 38]
rez=select(lambda x: (x,x**2),rez) # Функция lambda возвращает кортеж из элеменов (x,x**2), где x-  принимает значение элементов списка rez
print(rez)                         #[(2, 4), (8, 64), (38, 1444)]

#///////////////////////////////////////////////////////////////////////////////////////////
print('Задачa.1  через функции: map, filter-----------------------')
rez=list(map(int,data))  # перевели в тип int все числа списка data
print(rez)                        # [1, 2, 3, 5, 8, 15, 23, 38]
rez=list(filter(lambda x: x%2==0, rez))  # Взвращаем список из элементов списка rez, для которых lambda функция = true
print(rez)                        #[2, 8, 38]
rez=list(map(lambda x: (x,x**2),rez)) # Функция lambda возвращает кортеж из элеменов (x,x**2), где x-  принимает значение элементов списка rez
print(rez)  

#/////////////////////////////////////////////////////////////////////////////////////////

print('Функция map-----------------------')
# Функция map() применяет указанную функцию к каждому элементу итерируемого объекта и
#возвращает итератор с новыми объектами. map() позволит избавиться от функции select.

list_1 = [x for x in range (1,20)]
list_1 = list(map(lambda x: x + 10, list_1 )) # map() позволит избавиться от функции select.
print(list_1)  # [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

print('ЗАДАЧА.2._ФУНКЦИЯ map-----------------------')
# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя используется
# пробел. Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?
data = '1 2 3 5 8 15 23 38'.split()
print(data) # ['1', '2', '3', '5', '8', '15', '23', '38']
print('Введите числа через пробел: ')
data = list(map(int,input().split())) # функция int применяется к каждому элементу списка input().split(). Введенная строка преобразуется в список функцией split()
print(data)
#////////////////////////////////////////////////////////////////////////////////////////

print('ФУНКЦИЯ filter-----------------------')
# Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для которых функция вернула True.
data = [x for x in range(10)]
print(data)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
res = list(filter(lambda x: x % 2 == 0, data)) # filter() позволит избавиться от функции where, которую мы писали ранее
print(res) # [0, 2, 4, 6, 8]

print('filter пример2')
data=[15, 20, 25, 175, 19, 23]
res=list(filter(lambda x: x%10==5,data))
print(res)

#///////////////////////////////////////////////////////////////////
print('функция zip----------------')
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
print('users:', users)
print('ids:', ids)
print('salary:', salary)
data = list(zip(users, ids, salary)) #  возвращает итератор с кортежами
print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]

#///////////////////////////////////////////////////////////////////
print('функция enumerate----------------')
users = ['user1', 'user2', 'user3']
data = list(enumerate(users)) # Функция enumerate() позволяет пронумеровать набор данных. возвращает новый итератор с
                              # кортежами из индекса и элементов входных данных
print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3')]
