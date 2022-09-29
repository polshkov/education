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
'''
name = input('Your name: ')
age = input('Your ag: ')
print('Hi, ' + name + '!\nYou are already ' + age + ' years old.')
'''

# ** - возведение в степень
a = 4
b = 2
c = b ** a
print ("**: " + str(c))

# % - деление по модулю (остаток от деления), // - целочисленное деление (частное)
a = 10
b = 3
c = a % b
print ("%: " + str(c))
c = a // b
print ("//: " + str(c))

# Списки
names = ["Igor", "Olga", "Kate"]
print(names[len(names)-1]) # Выводит последний элемент списка, [0] - выводит первый
print(str(len(names)) + " Names: " + ', '.join(names))

# циклы
x = 1
while x <= 10:
  if x%2 == 0: # делит на четные (even) и нечетные (odd) числа
    print(str(x) + " is even")
  else:
    print(str(x) + " is odd")
  x += 1

'''You are making a ticketing system.
The price of a single ticket is $100.
For children under 3 years of age, the ticket is free.

Your program needs to take the ages of 5 passengers as input and output the total price for their tickets.

Sample Input
18
24
2
5
42

Sample Output
400 '''

total = 0
i = 0
while i < 5:
    age = input()
    if int(age) > 3:
        total += 100
    i += 1
print(total)

i = ["hello", "world", "spam", "eggs"]
for y in i[3:]:
  print(y + "!")

# Поменять буквы в словах (o -> u, l -> y) с помощью цикла for
i = "Hello world"
fin = ""
for char in i:
    if char == "o":
        fin += "u"
    elif char == "l":
        fin += "y"
    else:
        fin += char
print(fin)

# Поменять буквы в словах (o -> u, l -> y) с помощью цикла while
text = "Hello world"
fin = ""
i = 0
while i < len(text):
    if text[i] == "o":
        fin += "u"
    elif text[i] == "l":
        fin += "y"
    else:
        fin += text[i]
    i += 1
print(fin)

# Поменять буквы в словах (o -> u, l -> y) с помощью replace
i = "Hello world"
a = i.replace("l","y")
y= a.replace("o","u")
print(y)

'''BMI Calculator
Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight.
It’s calculated using a person's weight and height, using this formula: weight / height²

The resulting number indicates one of the following categories:
Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more

Let’s make finding out your BMI quicker and easier, by creating a program that takes a person's weight and height as input and outputs the corresponding BMI category.

Sample Input
85
1.9

Sample Output
Normal '''

wg = input()
hg = input()
bmi = int(wg) / float(hg)**2
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obesity")

# округление
x = 5.65
print(round(x)) # стандартное округление
import math # Импортируем библиотеку
print(math.ceil(x)) # округление в большую сторону
print(math.floor(x)) # округление в меньшую сторону