# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

list_1 = [-6, 1, 3, 5, 7]
k = 6
rez=list_1[0]
r=abs(k-list_1[0])
for i in list_1:
    if abs(k-i)<r:
        rez=i
        r=abs(k-i)
print(rez)