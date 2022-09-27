# str (string, строка)
text = "Slava Ukraini"
name = "Oleg"

# float (Вещеественное, действи́тельное число, обладающее дробной частью)
fnumb = 5.7
# int (integer, целочисленное, целое число)
numb = 6
age = 22
# bool (булевое значение) только True, False
status = True

# функция(команда) принимает аргументы
print(text)

# Экранирование \
print("He's a \"Hero\"")
print('He\'s a "Hero"')

# Перевод строки \n
print('\nHello\nWorld\n')

# Конкатенация, тайпкастиг
print('Hello, my name is ' + name + '!')
print("I'm " + str(age) + " years old.")

### Запрос данных от пользователя input
#name = input('Your name: ')
#age = input('Your ag: ')
#print('Hi, ' + name + '!\nYou are already ' + age + ' years old.')

# ** - возведение в степень
a = 4
b = 2
c = b ** a
print ("**: " + str(c))

# % - деление по модулю ()
a = 10
b = 3
c = a % b
print ("%: " + str(c))
c = a // b
print ("//: " + str(c))

'''This
is
a comment too'''

# Списки
names = ["Igor", "Olga", "Kate"]
print(names[len(names)-1]) # Выводит последний элемент списка, [0] - выводит первый
print(str(len(names)) + " Names: " + ', '.join(names))
