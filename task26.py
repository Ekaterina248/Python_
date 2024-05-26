
# dictionary.items() выводит список, где каждый элемент-кортеж из двух элементов: Ключ, Значение

dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
f=dictionary.items()            # <class 'dict_items'>
print('f=',f)                   # f= dict_items([('up', '↑'), ('left', '←'), ('down', '↓'), ('right', '→')])
print(type(f))                  #<class 'dict_items'>
print(type(dictionary))         # <class 'dict'>

# dictionary.get('up',0) функция возвращает значение ключа i. 
#если такого ключа нет, то фунуция=0,
# заместо 0 можно выводить в случае ошибки любое значение
print (dictionary['up'])        # ↑
print(dictionary.get('up',0))   # ↑
print(dictionary.get('up1','ошибка')) #ошибка
print(dictionary.get('up1',0))   #ошибка
#-------------------
c=[1,2,3,4]
print (type(c))   #<class 'list'>
c={1,2,3,4}
print (type(c))   #<class 'set'>
c='123456'
print (type(c))   #<class 'str'>
#--------------------
m = '345'
print(m * 2) # 2 раза повторит строку m 345345
print(int(m)*2)
