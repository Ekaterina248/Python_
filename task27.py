# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13
s="shells   I'm sure.So if   she sells sea   S s S s"
s=s.lower()
print(s)
s1=set(s.split()) # перевод строки в список (по пробелам по умолчанию, но можно задать другой раделитель)
print(s1)
print(len(s1))


                  