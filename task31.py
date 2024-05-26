# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0= 0, 
# a1= 1, 
# ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# 0 1 1 2 3 5 8 13 21 34 55  89
#   1 2 3 4 5 6 7  8  9  10  11

print('РЕШЕНИЕ1. через рекурсию-----------')
def fib1(n):
    if n in [1, 2]: # базис. условие выхода
        return 1
    return fib1(n - 1) + fib1(n - 2)
n1=int(input('Введите n:'))

print(f'Fib1({n1})={fib1(n1)}')

print('РЕШЕНИЕ2. Без рекурсии-----------')
def fib2(n):
    i1=1
    i2=1
    f=1
    i=2
    while i<n:
        f=i1+i2
        i1=i2
        i2=f
        i=i+1
    return f    


print(f'Fib2({n1})={fib2(n1)}')