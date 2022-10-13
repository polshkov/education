# Most Important String Methods
y = " This is lazy\t\n "
print(y.strip())  # Remove Whitespace: 'This is lazy'
print("DrDre".lower())  # Lowercase: 'drdre'
print("attention".upper())  # Uppercase: 'ATTENTION'
print("smartphone".startswith("smart"))  # True
print("smartphone".endswith("phone"))  # True
print("another".find("other"))  # Match index: 2
print("cheat".replace("ch", "m"))  # 'meat'
print(','.join(["F", "B", "I"]))  # 'F,B,I'
print(len("Rumpelstiltskin"))  # String length: 15
print("ear" in "earth")  # Contains: True

# Indexing and Slicing
s = "The youngest pope was 11 years old"
print(s[0])  # 'T'
print(s[1:3])  # 'he'
print(s[-3:-1])  # 'ol'
print(s[-3:])  # 'old'
x = s.split()  # creates string array of words
print(x[-3] + " " + x[-1] + " " + x[2] + "s")  # '11 old popes'

# Экранирование \
print("He's a \"Hero\"")
print('He\'s a "Hero"')

"""
These are whitespace characters in strings.
● Newline \n
● Tab \t
"""
print('\tHello\n\tWorld')

# Arithmetic Operations
x, y = 3, 2
print(x + y)  # = 5
print(x - y)  # = 1
print(x * y)  # = 6
print(x / y)  # = 1.5
print(x // y)  # = 1 - целочисленное деление (частное)
print(x % y)  # = 1 - деление по модулю (остаток от деления)
print(-x)  # = -3
print(abs(-x))  # = 3
print(int(3.9))  # = 3
print(float(3))  # = 3.0
print(x ** y)  # = 9

# Списки
names = ["Igor", "Olga", "Kate"]
print(names[len(names)-1])  # Выводит последний элемент списка, [0] - выводит первый
print(str(len(names)) + " Names: " + ', '.join(names))

# The count() method returns the number of elements with the specified value
# Syntax: list.count(value)
fruits = ["apple", "banana", "cherry", "cherry"]
x = fruits.count("cherry")
print(x)  # 2

points = [1, 4, 2, 9, 7, 8, 9, 3, 9]
x = points.count(9)
print(x)  # 3

# циклы
x = 1
while x <= 10:
    if x % 2 == 0:  # делит на четные (even) и нечетные (odd) числа
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
    age = 18
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

# Python One Line Elif
x = 42

print("no") if x > 42 else print("yes") if x == 42 else print("maybe")  # yes

# округление
x = 5.65
print(round(x))  # стандартное округление
import math  # Импортируем библиотеку
print(math.ceil(x))  # округление в большую сторону
print(math.floor(x))  # округление в меньшую сторону

N = 10
res = list(range(0, N+1))
print(sum(res))

# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)

# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы одним списком, которые меньше 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = ''
for i in a:
    if i < 5:
        b += str(i)
    else:
        continue
print(list(b))
print([elem for elem in a if elem < 5])

# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
q = []
for i in a:
    for t in b:
        if i == t:
            q += [i]
print(q)  # вариант решения №1
q2 = []
for i in a:
    if i in b:
        q2 += [i]
print(q2)  # вариант решения №2
print([elem for elem in a if elem in b])  # вариант решения №3

x = 41
print("no") if x > 42 else print("yes") if x == 42 else print("maybe")

# Выведите первый и последний элемент списка.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([a[0]] + [a[-1]])
print(f'Первый: {a[0]}; последний: {a[-1]}')

# The append() function is used to add an item to the end of the list:
a = [1, 1, 2, 3]
a.append(4)
a += [6]
print(a)

# index() finds the first occurrence of a list item and returns its index.
nums = [9, 8, 7, 6, 5]
print(nums.index(5))

# Any code placed after the return statement won’t be executed.
def add_numbers(x, y):
    tot = x + y
    return tot
    print("This won't be printed")
print(add_numbers(4, 5))

# моржовый оператор (walrus)
print(num := int('2'))

""" Найдите индекс элемента "strawberry" в списке """
fruits = ["apple", "mango", "strawberry", "pomegranate", "melon"]
target = "strawberry"
for i in range(len(fruits)):
    if fruits[i] == target:
        print(f"{target} found at index {i}")  # strawberry found at index 2

""" Single-Line For Loop """
for i in range(10):  # вариант записи №1
    if i<5:
        j = i**2
    else:
        j = 0
    print(j)
for i in range(10): print(i**2 if i<5 else 0)  # вариант записи №2

""" Single line for-loop to build a list """
squares = []  #---------------------------------------------------------  # вариант записи №1
for i in range(10):
    squares.append(i ** 2)
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print([i**2 for i in range(10)])  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]  # вариант записи №2

k = 998887
pol1 = int(k) // 1000  # 998
pol2 = int(k) % 1000   # 887
print([str(x) for x in str(k)])  # ['9', '9', '8', '8', '8', '7']
print([int(x) for x in str(k)])  # [9, 9, 8, 8, 8, 7]

n = '99'
y = [str(i) for i in n]
print(' '.join(y))  # 9 9

""" Single line for-loop to build a dictionary """
bigList = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
data = {}
for i in bigList:
    data[i] = i
print(data)
print({i: i for i in bigList})
print(dict((i, i) for i in bigList))

""" Метод dict.get()
dict.get(key[, default])
Возвращает значение для ключа key, если ключ находится в словаре,
если ключ отсутствует то вернет значение default """
nums = [9,4,9,8,4,9]
ndict = {}
ndict2 = {}
for i in nums:
    if i not in ndict:
        ndict[i] = 1
    else:
        ndict[i] += 1
print(ndict)         # {9: 3, 4: 2, 8: 1}
for i in nums: ndict2[i] = ndict2.get(i, 0) + 1
print(ndict2)        # {9: 3, 4: 2, 8: 1}

# Функция enumerate(sequence, start=0)
s = [10, 20, 30, 40]
y = list(enumerate(s))                  # [(0, 10), (1, 20), (2, 30), (3, 40)]
d = dict(y)                             # {0: 10, 1: 20, 2: 30, 3: 40}
print({v: k for k, v in d.items()})     # {10: 0, 20: 1, 30: 2, 40: 3}
print({v: k for k, v in enumerate(s)})  # {10: 0, 20: 1, 30: 2, 40: 3}


# One-line expression to map dictionary to another
d = {'user_id':1, 'user':'user1', 'group_id':3, 'group_name':'ordinary users'}
m = {'user_id':'uid', 'group_id':'gid', 'group_name':'group'}
print(dict((m.get(k, k), v) for (k, v) in d.items()))
# {'uid': 1, 'user': 'user1', 'gid': 3, 'group': 'ordinary users'}


