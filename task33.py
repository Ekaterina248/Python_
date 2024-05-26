# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
n=int(input('Введите кол-во оценок: '))
list1=[]
for i in range(n):
    list1.append(int(input()))
print(list1)
max_oz=max(list1)
min_oz=min(list1)
print(max_oz,min_oz)

for i in range(len(list1)):
    if list1[i]==max_oz:
        list1[i]=min_oz
print(*list1)        

