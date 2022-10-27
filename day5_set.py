# a = set()
# print(type(a))

# a.add(2)
# a.add(4)
# a.update([1, 123 ,345, 13])


# методы удаления
# print(a.pop())
# a.remove('asd')
# a.clear()
# a.discard('menya netu, no mne poh')

# методы сравнения

# a = {2, 'qwerty', 31, 43, 'asd', 2}
# b = {21, 'qwert', 3, 4, 'asd', 2}

# print(b.difference(a))
# print(a.intersection(b))
# print(a.intersection_update(b))
# print(a)

# a.difference_update(b) 
# print(a)
# print(b)


# a = {2, 'qwerty', 31, 43, 'asd', 2}
# b = {21, 'qwert', 3, 4, 'asd', 2}

# print(a)
# a.difference_update(b)
# print(a)


# from audioop import add
# from curses.ascii import isdigit
# 
# from re import A


# a = {}
# # методы добавления
# # a.update(
# #     {
# #         1: 21,
# #         [1, 2, 3, 4]
# #     })
# # print(a)


# # a.update({1:32})
# # a['hello']={"key":"world", 'daniyar daraboz', '1465'}

# print(a["hello"]['key'])
# users = {
#     "users1":{
#         "name": "Asan",
#         'age': '14',
#         'phone': '8 747 936 4480',
#         'language': 'python'
#     },
# '010226500955': {
#     "name": "Usen",
#     'age': "15",
#     'phone': '87700 962 6469',
#     'language':'python'
#     }
# }

# print(users.get('010226500955'))
# print(users['010226500955'])
# print(users.values())
# print(users.items())

# from pprint import pprint
# print(users['010226500955']['name'])
# print(users)

# users = [('roma', '12345')]

# login = input('put login: ')
# password = input('put pass: ')
# password_confirm = input('put pass again 667: ')

# # login = 'roma'

# if not login.isdigit() and not login.isalpha():
#     if password == password_confirm:
#         users.append((login, password))


# a = {}
# users = {
#     "users1":{
#         "name": "Asan",
#         'age': '14',
#         'phone': '8 747 936 4480',
#         'language': 'python'
#     },
# '010226500955': {
#     "name": "Usen",
#     'age': "15",
#     'phone': '87700 962 6469',
#     'language':'python'
#     }
# }
# users.pop('010226500955')
# print(users)

# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia','Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']

# print(list(set(south_american_countries)))


# a = {"dog", "cat", "mouse", "sheep"}
# b = {"cow", "horse", "donkey", "cat", "dog"}
# # print(a.intersection_update(b))
# print(a.difference_update(b))
# print(a)

# puple = {
#     'many' : 'lawyer',
#     'sins' : 'doctor',
#     'gustavo' : 'drugdealer',
#     'jamal' : 'killer',
#     'kiri' : 'teacher'
# }

# for key, value in puple.items():
#     print(f"zdrastvuite {key}! good job {value}")


# my_friends = {
#     "Joomart": "+77555246810",
#     "Adinai": "+77555013579",
#     "Ermek": "+77777013579",
#     "Atai": "+77777246810",
#     "Alymbek": "+77555501234",
# }

# her_friends = {
#     "Lyazat": "+77551123456",
#     "Salavat": "+77552234567",
#     "Daniyar": "+77553345678",
#     "Bolot": "+77554456789",
#     "Alymbek": "+77555501234",
#     "Dastan": "+77556678912",
#     "Maksat": "+77557789012",
#     "Adinai": "+77555013579",
# }
# our_friends = {}
# from pprint import pprint
# our_friends.update(my_friends)
# our_friends.update(her_friends)
# pprint(our_friends)


# his_her_friends = {
#     'Lyazat',
#     'Salavat',
#     'Daniyar',
#     'Bolot',
#     'Alymbek',
#     'Dastan',
#     'Maksat',
#     'Adinai',
# }

# my_friends = {
#     "Joomart",
#     "Adinai",
#     "Ermek",
#     'Bolot',
#     'Alymbek',
#     'Dastan',
#     "Atai",
#     "Alymbek",
# }
# print(my_friends.intersection(his_her_friends))
# print(my_friends)

# from re import L


# list_1 = []
# list_1.append(input('put: '))
# list_1.append(input('put: '))
# print(list_1)


# def get_string_length_diff(string1,string2):
#     return len(string1)-len(string2)
 
# print("Enter two strings:")
 
# str1=input()
# str2=input()
 
# strings_deff = get_string_length_diff(str1 ,str2)
  
# if strings_deff==0:
#     print("Они равны")
# elif strings_deff>0:
#     print("Строка '", str1, "' больше строки '", str2, " 'на ", strings_deff, " символов.")
# elif strings_deff<0:
#     print("Строка '", str2, "' больше строки '", str1, "'на ", -strings_deff, " символов.")

# a = input('put: ')
# b = input('put: ')
# if len(a) != len(b):
#     print(len(b) - len(a) if len(b) > len(a) else len(a) - len(b))
# else:
#     print('Они равны')


# (2 > 3) and (3 < 4) or True
# (not True or 5**2 != 1000) and not False
# not ((None == False) and (25 >= 25)) and ("123" == 123)
# Пример выполнения задания:
# False or (True or (2 < 3))
# False or (True or True)
# False or True
# True


# s = input("знак('+', '-', '*', '/', '//', '%'): ")
# a = float(input('a = '))
# b = float(input('b = '))

# if s == '+':
#     print(a + b)
# elif s == '-':
#     print (a - b)
# elif s == '*':
#     print(a * b)
# elif s == '/':
#     if b != 0:
#         print(a / b)
# elif s == '//':
#     print(a // b)
# elif s == '%':
#     print(a % b)
# else:
#     print('delenie na nolb!')


from curses.ascii import isalpha


# a = [input(), input(), input()]
# s = ''.join(a)

# if len(s) > 20 and s.isalpha():
#     # mx = max(a, key=len)
#     mx = a[0] if len(a[1]) < len(a[0]) > len(a[2]) else a[1] if len(a[0]) < len(a[1]) > len(a[2]) else a[2]
#     a.remove(mx)

# mail_input = input('Put ur email: ')

# if mail_input.endswith('gmail.com')  or mail_input.endswith('mail.ru'): 
#     num = int(input('Put num 666999: '))
#     if num == 666999:
#         print('Success')
#     else: 
#         print('Error')
# else:
#     print('Your e-mail is incorrect')










