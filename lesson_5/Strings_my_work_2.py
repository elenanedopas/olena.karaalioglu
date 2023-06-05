greeting = 'Hello Python!'
greeting_length = len(greeting)
print(len(greeting))

# INDEXING
# Якщо я хочу получити елемент з певним індексом (а Індексація у Пайтоні починається з нуля)
# то я вказую у квадратних дужках індекс елементу
print(greeting[0])
print(greeting[3])
print(greeting[6])

#якщо нам потрібно отримати якийсь елемент з кіня строки
# то потрібно вказати "мінус"+ індекс - типу -1 (перший елемент з кінця)
print(greeting[-1])
print(greeting[-2 ])

#форматування за допомгою FORMAT
sentence = '{what} my dear {who}'
print(sentence.format(what = "hello", who = "friend"))

#форматування за доп. f-string
name = 'Jane'
surname = 'Bennet'
my_favorite = f'My favorite student is {name} {surname}'
print(my_favorite)
