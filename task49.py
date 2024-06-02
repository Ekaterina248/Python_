# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
#print(*find_farthest_orbit(orbits))
# вывод: 2.5 10

print('МОЁ РЕШЕНИЕ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
from math import pi
#pi=3.14
#Список с площадями орбит///////////////////////////
# s_orbits=[]
# for i in orbits:
#     s_orbits.append(i[0]*i[1]*pi)
# print(s_orbits)  
#Список с площадями орбит. lambda ///////////////////////////
#s_orbits=list(map(lambda x: (x[0]*x[1]*pi),orbits))   
#print(s_orbits)
orbits=[x for x in orbits if x[0]!=x[1]]
s_orbit_max=max(list(map(lambda x: (x[0]*x[1]*pi),orbits)))
#print(s_orbit_max)
rez=list(filter(lambda x: x[0]*x[1]*pi==s_orbit_max, orbits))
print(rez[0][0], rez[0][1])
#print(rez)
#print(type(rez))

print('МОЁ РЕШЕНИЕ_2 способ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#pi=3.14
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
def find_farthest_orbit(orbits):
    orbits=[x for x in orbits if x[0]!=x[1]]
    s_orbit_max=max(list(map(lambda x: (x[0]*x[1]*pi),orbits)))
    rez=list(filter(lambda x: x[0]*x[1]*pi==s_orbit_max, orbits))
    return rez
print(*find_farthest_orbit(orbits))

print('РЕШЕНИЕ НА СЕМИНАРЕ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
def find_farthest_orbit_new(list_of_orbits):
    list1=[i for i in list_of_orbits if i[0]!=i[1]]
    list_s=[(pi*i[0]*i[1]) for i in list1]
    max_s=list_s.index(max(list_s))
    return list1[max_s]

print(*find_farthest_orbit_new(orbits))

