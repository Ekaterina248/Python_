# Задача №1. 

# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

n=int(input('Введите сколько км машина проезжает за день: '))
m=int(input('Введите длину пути в км: '))
print('Чтобы проехать ',m,'км','потребуется',(m+n-1)//n,'дн.')