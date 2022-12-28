# Д/З 6
# 1. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

# Old version 
# n = list('1, 1, 2, 3, 4, 4, 4')
# list = n
# list_count = [ ]
# for i in list:
#     count = 0
#     for k in list:
#         if k == i:
#             count += 1
#     list_count.append(count)
# result = [ ]
# for i in range(len(list_count)):
#     if list_count[i] == 1:
#         result.append(list[i])
# print(result)

# New version
# n = list('1, 1, 2, 3, 4, 4, 4')
# n1 = list(filter(lambda x: n.count(x) == 1, n))    
# print(n1)

# 2. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

# Old version 
# def sum (num):
#     sum = 0
#     for i in num:
#         if i != '.':
#             sum = sum + int(i)
#     return sum
# num = input('Введите вещественное число: ')
# print (sum(num))

# New version 
# print(sum(list(map(lambda x: 0 if x == '.' else int(x), input('Введите вещественное число: ')))))

# 3. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Old version 
# text = 'абв'
# my_str = input("Введите текст через пробел: ") 
# no_text = " "
# for char in my_str:
#    if char not in text:
#        no_text = no_text + char
# print(f'Результат:{no_text}')

# New version 
# text = 'абв'
# x = input("Введите текст через пробел: ") 
# list = list(filter(lambda x: x not in text, x))
# print (list)
