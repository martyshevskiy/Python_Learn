# Напишите функцию summa_n, которая принимает одно целое положительное t число и находит сумму всех
# чисел от 1 до t включительно.
# Программа должна распечатать сообщение
# "Я знаю, что сумма чисел от 1 до {t} равна {S}", где в качестве t и S вам необходимо подставить значения
# (см. тестовые данные)
# Ваша задача написать только определение функции summa_n, вызывать ее не нужно

# def summa_n(t):
#     summa = 0
#     for i in range(1, t+1):
#         summa += i
#     print(f'Я знаю, что сумма чисел от 1 до {t} равна {summa}')

# -------------------------------------------------------------------

# Напишите функцию sum_num для суммирования всех цифр строки.
# Функция должна принимать строку, суммировать все ее символы, которые являются цифрами,
# и в качестве ответа выводить найденную сумму.

# ff= 'sdf'
# def sum_num(text):
#     summa = 0
#     for i in text:
#         if i.isdigit():
#             summa += i
#     print(summa)

# -------------------------------------------------------------------

'''Напишите функцию get_body_mass_index,
которая принимает массу тела человека в кг и рост в см и рассчитывает индекс массы тела человека по формуле
'''

# def get_body_mass_index(kg, growth):
#     index = kg / (growth / 100)**2
#     if index < 18.5:
#         print('Недостаточная масса тела')
#     elif 18.5 <= index <= 25:
#         print('Норма')
#     else:
#         print('Избыточная масса тела')

# -------------------------------------------------------------------

'''Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на экран результат проверки.
Сложным паролем будет считаться комбинация символов, в которой :
Есть хотя бы 3 цифры
Есть хотя бы одна заглавная буква 
Есть хотя бы один символ из следующего набора "!@#$%*"
Общая длина не менее 10 символов
Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password", в противном случае - "Easy peasy"'''

# def check_password(password):
#     upper = False
#     special_char = False
#     digits = 0
#     if len(password) >= 10:
#         for i in password:
#             if i.isdigit():
#                 digits += 1
#             elif i in '!@#$%*':
#                 special_char = True
#             elif i.isupper():
#                 upper = True
#     if digits >= 3 and upper and special_char:
#         print('Perfect password')
#     else:
#         print('Easy peasy')

# -------------------------------------------------------------------

'''Создайте функцию count_letters, которая принимает на вход фразу и подсчитывает, 
какое количество в ней строчных(K) и заглавных (N) букв, все остальные символы игнорируются. 
Функция должна вывести на экран информацию о найденных буквах в определенном формате. 
Количество заглавных символов: N
Количество строчных символов: K'''

# def count_letters(text):
#     lower = 0
#     upper = 0
#     for i in text:
#         upper += i.isupper()
#         lower += i.islower()
#     print(f'Количество заглавных символов: {upper}\nКоличество строчных символов: {lower}')

