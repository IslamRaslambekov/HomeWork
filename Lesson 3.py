
# Задача 1 (Методами строк очистить текст от знаков препинания)

# file = open('Text.txt', encoding = 'utf-8')
# initial_text = file.read()
# no_need = '«!.,—;?»-()'
# for i in no_need:
#     initial_text=initial_text.replace(i, " ")
# print(initial_text)


# Задача 2 ( Сформировать list со словами (split))

# file = open('Text.txt', encoding = 'utf-8')
# initial_text = file.read()
# initial_text=initial_text.split()
# print(initial_text)

# Задача 3.1 (Привести все слова к нижнему регистру (map))
#
# file = open('Text.txt', encoding = 'utf-8')
# initial_text = file.read()
# only_lower=list(map(lambda x:x.lower(),initial_text))
# print(type(only_lower))


# Задача 3.2 (Получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;)

# file = open('Text.txt', encoding = 'utf-8')
# initial_text = file.read()
# initial_text=initial_text.split()
# repeat_dict={}
# b=0
# for a in initial_text:
#     sum_repeat=repeat_dict.get(a, b)
#     repeat_dict[a]=sum_repeat+1
# print(repeat_dict)


# Задача 4 (Вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set)).

# initial_text = list(text_dict.items())
# print(initial_text)
# initial_text.sort(key=lambda i:i[1], reverse=True)
# print(initial_text[:5])
