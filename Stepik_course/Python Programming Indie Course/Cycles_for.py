'''Программа принимает на вход натуральное число N.
Ваша задача вывести на экран все числа от 1 до N каждое число на отдельной строке. '''

# n = int(input())
# for i in range(1, n + 1):
#     print(i)

'''-------------------------------------'''

'''Напишите программу, которая выведет все элементы арифметической прогрессии от 0 до 500 включительно с шагом 5.
Каждый элемент выводится отдельно на своей строке в таком виде'''

# for i in range(0, 501, 5):
#     print(i)

'''-------------------------------------'''

'''Программа принимает на вход натуральное число N. 
Ваша задача вывести на экран все числа от N до 1 в сторону уменьшения каждое число на отдельной строке. '''

# n = int(input())
# for i in range(n, 0, -1):
#     print(i)

'''-------------------------------------'''

'''Каждый, кто смотрел Симпсонов, помнит, что в начале любой серии Барт писал забавные фразы на доске.
Давайте и мы напишем подобную программу. 
На вход ей будет поступать фраза и затем количество раз, которое эту фразу нужно повторить.'''

# text = input()
# num = int(input())
# for i in range(num):
#     print(text)

'''-------------------------------------'''

'''Напишите программу, которая считывает два натуральных числа a и b (гарантируется, что a<b), 
после чего для всех чисел от a до b включительно выводит:
“Fizz”, если это число делится на 3;
“Buzz”, если это число делится на 5;
“FizzBuzz”, если выполнены оба предыдущих условия;
само это число в остальных случаях.'''

# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

'''-------------------------------------'''

'''Давайте составим сводную информацию о квадратах и кубах интервала чисел.
На вход программе подается два натуральных числа a и b (гарантируется, что a<b), 
после чего для каждого целого числа на интервале от a до b включительно необходимо вывести фразу следующего вида:
«Число {число}; его квадрат = {квадрат}; его куб = {куб}»
Кавычки выводить не нужно и пользуйтесь f-строкой.'''

# a, b = int(input()), int(input())
# for i in range(a, b + 1):
#     print(f'Число {i}; его квадрат = {i**2}; его куб = {i**3}')

'''-------------------------------------'''

'''Если перечислить все натуральные числа ниже 10, которые кратны 3 или 5, то получим 3, 5, 6 и 9. 
Сумма этих чисел 23.
Напишите программу, которая принимает натуральное число n и находит 
сумму всех чисел ниже переданного числа n, которые делятся на 3 или на 5.
'''

# n = int(input())
# summa = 0
# for i in range(n):
#     if i % 3 == 0 or i % 5 == 0:
#         summa += i
# print(summa)

'''-------------------------------------'''

'''Напишите программу, которая найдет сумму кубов натуральных чисел от 50 до 100 включительно'''

# summa = 0
# for i in range(50, 101):
#     summa += i**3
# print(summa)

'''-------------------------------------'''

'''Стандартная задача на нахождения факториала. Факториал числа n! обозначается и находится по формуле '''

# n = int(input())
# factorial = 1
# if n == 0 or n == 1:
#     print(factorial)
# else:
#     for i in range(1, n+1):
#         factorial *= i
#     print(factorial)

'''-------------------------------------'''

'''Правила её очень просты: сначала определяется значение n — количество раундов игры. 
В очередном раунде каждый из игроков один раз бросает стандартный игральный кубик, 
на грани которого нанесены различные числа от 1 до 6. 
Игрок, выбросивший большее значение, становится победителем в раунде. 
В случае, если выпавшие значения равны, победа не засчитывается никому.
В самой же игре побеждает участник, выигравший в большем количестве раундов. 
Если же количества побед, заслуженных игроками, равны, то объявляется ничья.

В первой строке входных данных содержится число n (1≤n≤100) — количество раундов игры.
Следующие n строк содержат описание раундов. 
В i-й из них содержится пара целых чисел mi и ci (1≤mi,ci≤6) — результаты бросков Мишки и Криса в i-ом раунде соответственно.'''

# round_count = int(input())
# mishka = 0
# kris = 0
# for i in range(round_count):
#     m, k = map(int, input().split())
#     if m > k:
#         mishka += 1
#     elif m < k:
#         kris += 1
#     else:
#         mishka += 1
#         kris += 1
# if mishka > kris:
#     print('Mishka')
# elif mishka < kris:
#     print('Chris')
# else:
#     print('Friendship is magic!^^')

'''-------------------------------------'''

'''Найдите, в каких строках из введённых и в каком месте упоминается "рок", причем регистр букв не важен.
Вместо явного цикла прохода по строке в цикле используйте подходящий метод строки

Для каждой строки, в которой есть сочетание символов «рок», 
нужно вывести (в порядке появления таких строк) номер этой строки (нумерация начинается с единицы) и номер символа, 
с которого начинается первое вхождение этой подстроки (нумерация символов также с единицы).'''

# num = int(input())
# for i in range(num):
#     stroka = input().lower()
#     if 'рок' in stroka:
#         print(i + 1, stroka.index('рок') + 1)

'''-------------------------------------'''

'''Предположим, вы переписываете у друга рецепты в блокнотик, но вам не нравится "соль". Переписывайте без этого слова.
Одна строка — пункты рецепта, разделённые запятой и пробелом, без пунктов с упоминанием слова "соль" 
(то есть таких, в которых нет подстроки "соль" в нижнем регистре).'''

# num = int(input())
# result = ''
# for i in range(num):
#     punkt = input()
#     if 'соль' in punkt:
#         continue
#     result += punkt + ',' + ' '
# print(result[:-2])

'''-------------------------------------'''

'''Иногда некоторые слова вроде «civilization» или «internationalization» настолько длинны, 
что их весьма утомительно писать много раз в каком либо тексте.
Будем считать слово слишком длинным, если его длина строго больше 10 символов. 
Все слишком длинные слова можно заменить специальной аббревиатурой.
Эта аббревиатура строится следующим образом: записывается первая и последняя буква слова, 
а между ними — количество букв между первой и последней буквой (в десятичной системе счисления и без ведущих нулей).
Таком образом, «civilization» запишется как «c10n», а «internationalization» как «i18n».
Вам предлагается автоматизировать процесс замены слов на аббревиатуры. 
При этом все слишком длинные слова должны быть заменены аббревиатурой, 
а слова, не являющиеся слишком длинными, должны остаться без изменений.'''

# num = int(input())
# for _ in range(num):
#     word = input()
#     if len(word) > 10:
#         print(word[0] + str(len(word[1:-1])) + word[-1])
#     else:
#         print(word)

'''-------------------------------------'''















