# print(5, 8, 6)
# n=5
# print(n)
# print(type(n))
# n='папа'
# n1="мама"
# print(n)
# print(n1)
# print(type(n))

# a=5
# b=5.89
# c='hello'
# print (a,b,c)
# print(f"{a}-{b}-{c}")
# print("{}-{}-{}".format(a,b,c))

# print('Введите первое число:')
# a=int(input ())
# #print(a)
# #print(type(a))
# b=int(input('Введите второе число:'))
# print(f'{a}+{b}=')
# print(a+b)

# c=1
# print(c)
# print(type(c))
# c=bool(c)
# print(c)
# print(type(c))

# a=5.89956
# b=6.568
# print(round(a*b,2))
# if a>b:
#     print(f'max={a}')
# else:
#     print(f'max={b}')

# username=input('Введите имя:')
# if username=='Миша':
#     print('Ура!Это Миша')
# elif username=='Аня' :
#     print('Я люблю Анечку')
# elif username=='Катя':
#     print('Катюха')
# else:
#     print('Привет,',username)    

#----------------------------
# найти сумму цифр в числе
# n=1275
# sum=0
# while n>0:
#     sum=sum+n%10
#     n=n//10
# print(sum)

#--------------------------
#найти наименьший делитель

n=int(input('Введите число:'))
i=2
flag=True
while flag: #while flag==True
    if n%i==0:
        flag=False
        print('делитель =',i)
    elif i>n//2:    # делитель числа не может быть больш , чем число деленное на 2
        flag=False
        print('делитель =',n)
    i +=1

for i in range(100,0,-20):
    print(i)

for i in 'Katya':
    print(i)

text='Съешь ещё МолОка сегоДня или выпей'
print('длина строки=',len(text))                    #длина строки
print('eщё' in text)                #входит слово 'ещё' в строке текст
print(text.lower())                 #переводит все в нижний регистр
print(text.upper())                 #переводит все в верхний регистр
print(text.replace('ещё','ЕЩЁ'))    #заменить 'ещё' на 'ЕЩЁ'

print(text[2:10:2])             # выведет со 2 элемента по 10-1 с шагом2