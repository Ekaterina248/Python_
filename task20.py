# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его.
# Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.

k = 'КОТ'
print(k)
# 12
q={}
#A, E, I, O, U, L, N, S, T, R -1# А, В, Е, И, Н, О, Р, С, Т
s1='aeioulnstrавеинорст'
for i in s1:
    q[i]=1
# D, G – 2 очка;# Д, К, Л, М, П, У – 2 очка;
s2='dgдклмпу'
for i in s2:
    q[i]=2
# B, C, M, P – 3 очка; # Б, Г, Ё, Ь, Я – 3 очка;
s3='bcmpбгёья' 
for i in s3:
    q[i]=3
# F, H, V, W, Y – 4 очка;# Й, Ы – 4 очка;
s4='fhvwyйы'
for i in s4:
    q[i]=4
# K – 5 очков;# Ж, З, Х, Ц, Ч – 5 очков;
s5='kжзхцч'
for i in s5:
    q[i]=5
# J, X – 8 очков;# Ш, Э, Ю – 8 очков;
s8='jxшэю'
for i in s8:
    q[i]=8
# Q, Z – 10 очков.# Ф, Щ, Ъ – 10 очков.
s10='qzфщъ'
for i in s10:
    q[i]=10
#print(q)  
k=k.lower() # перевод слова в нижний регистр
print(k)
sum=0   
for i in k:
    #print(q[i])
    sum +=q[i]
print(sum)