
# 1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка (могут повторяться, можно взять значения:
# количество имен 20, N = 100, рекомендуется использовать функцию random);


# import random
#
# name = ['Michael', 'Sara', 'Kalie', 'John', 'Nina', 'Nicolas', 'Steven', 'Gina', 'Doris', 'Katya', 'Igor', 'Kim', 'Kevin', 'Ivan',
#         'Paul', 'Lily', 'Olivia', 'Isabella', 'Tom','Emily']
# n=100
#
# final_list=[]
# def seq (a,b):
'''
     1.Функция seq выполняет в случайной форме подбор обьектов из списка
     2.На вход в виде аргументов подаются a-(список) и b-(количество случайных обьектов из этого списка)

'''
#     for i in range(100):
#         final_list.append(random.choice(name))
#     return final_list
#
# print(seq(name,n))


# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;

# name_list=['Nika','Michael', 'Sara', 'Kalie', 'John', 'Nina','Steven', 'Gina', 'Doris', 'Katya', 'Igor', 'Kim', 'Kevin', 'Ivan',
#         'Paul', 'Lily', 'Olivia', 'Isabella', 'Tom','Emily','Nika','Emily']
# #
#
#
# def freq_name(names):
#     temp_dict = {}
#     freq_names = []
#     for i in names:
#         if i in temp_dict:
#             temp_dict[i] += 1
#         else:
#             temp_dict[i] = 1
#     for key, value in temp_dict.items():
#         if value == max(temp_dict.values()):
#             freq_names.append(key)
#     print('Самые часто встречающиеся слова {}'.format(freq_names))
# freq_name(name_list)

#
# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
#
# name = ['Michael', 'Sara', 'Kalie', 'John', 'Nina', 'Nicolas', 'Steven', 'Gina', 'Doris', 'Katya', 'Igor', 'Kim', 'Kevin', 'Ivan',
#         'Paul', 'Lily', 'Olivia', 'Isabella', 'Tom','Emily']
# #
# def un_word(names):
#     lst_word=[i[0] for i in names]
#     dct_word={key:lst_word.count(key) for key in lst_word}
#     temp = min(dct_word.keys())
#     print(dct_word)
#     print('Самая редкая первая встречающаяся буква -',format(temp))
#
#
# un_word(name)
#


# Задание 4



# from functools import reduce
#
# with open("log.txt", encoding="utf-8") as input_file:
#     elements_list = [elem.split(",")[0] for elem in input_file]
# print(max(elements_list))
