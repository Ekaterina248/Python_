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
print(out)
print('ЗАДАЧА.1._Lambda Fuction-----------------------')
def select(f,col):              # функция создает новый список из элементов f(x), где х - принимает значение элементов списка col
    return[f(x) for x in col]   # см. Генератор списка.

def where(f,col):                    # Взвращаем список из элементов списка col, для которых верно условие, заданное функцией f(x)
    return[x for x in col if f(x) ]  # см. Генератор списка. 

rez=select(int,data)   # перевели в тип int все числа списка data
print(rez)
rez=where(lambda x: x%2==0, rez) # Взвращаем список из элементов списка rez, для которых lambda функция = true
print(rez)
rez=select(lambda x: (x,x**2),rez) # Функция lambda возвращает кортеж из элеменов (x,x**2), где x-  принимает значение элементов списка rez
print(rez)

