# Задача №41. 
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: 1 2 3 4 5 Вывод: 0
# ВВод: 1 5 1 5 1 Вывод: 2

n=int(input('Введите длинну массива:'))
arr=[]
for i in range(n):
    arr.append(int(input()))
#arr=[1,10,3,48,25,35,24]
print(arr)
count=0
for i in range(1,len(arr)-1):
    if arr[i-1]<arr[i]>arr[i+1]:
        count +=1
print(count)        
