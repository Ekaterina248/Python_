# Задача №17. 
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.
#------------------------------------
# n=int(input('Введите длину списка:'))
# print('Введите элементы списка')
# list1=[]
# for i in range(n):
#     list1.append(input())
print('МОЕ РЕШЕНИЕ--------------------------------')
list1=[1,1,3,2,3,2,2,1,-4,-5,-6,-4]
n=len(list1)
print('list1=',list1)
list2=[]
list2.append(list1[0])
# print('list2=',list2)
flag=0
for i in range(1,n):
    for j in range(len(list2)):
        if list1[i]==list2[j]:
            flag=1
    if flag==0:
        list2.append(list1[i]) 
    flag=0
print('list2=',list2)   
res=len(list2)  
print('кол-во различных чисел=',res)    

print('РЕШЕНИЕ НА СЕМИНАРЕ--------------------')  
q=set(list1)
print('множество q=',q)
res=len(q)  
print('кол-во различных чисел=',res) 
print('кол-во различных чисел=',len(set(list1)))


