# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.
stroka = 'как ве-тер сме-ёт лис-ти'
stroka=stroka.lower()
list_stroka=stroka.split()
#print(list_stroka)
list_glasn='e y u i o a у е ы а о э я и ю'.split()
#print(list_glasn)
list_slog=[]
for slovo in list_stroka:
    col_slog=0
    for i in range(len(slovo)):
        if slovo[i] in list_glasn:
            col_slog +=1
    list_slog.append(col_slog)
#print(list_slog) 

if len(list_slog)==1:
    print('Количество фраз должно быть больше одной!')
else:
    flag=True
    for i in range(len(list_slog)-1):
        if list_slog[i]!=list_slog[i+1]:
            flag=False
    #print(flag)        
    if flag==True:
        print('Парам пам-пам')
    else:
        print('Пам парам')               