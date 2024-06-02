# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
values = [45,15,10,5]
def same_by(characteristic, objects):
    #list_1=list(map(characteristic,objects))  # мое решение
    list_1=[characteristic(x) for x in objects] # решение на семинаре
    print(list_1)
    flag=True
    for i in range(len(list_1)-1):
        if list_1[i]!=list_1[i+1]:
            flag=False
            
    return flag
    
print(same_by(lambda x: x %5,values))
if same_by(lambda x: x % 5, values):
    print('same')
else:
    print('different')
#same_by(lambda x: x % 2,values)
