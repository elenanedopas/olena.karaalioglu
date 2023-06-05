# 1.  List (Список):

#     a) Створіть пустий список і додайте до нього 3 різних числа. Виведіть список на екран.
some_list = [2, 5, 7, 3]
print (some_list)

#     б) Змініть значення другого елемента в списку. Виведіть оновлений список.
some_list[1] = 10
print(some_list)

#     в) Видаліть третій елемент зі списку. Виведіть оновлений список.
some_list.pop(2)
print(some_list)

#   г) Створіть другий список, з кількома числами більшими за 10.
#   Додайте в кінець першого списку. Виведіть на екран зріз списку від третього до п'ятого елементу.
new_list = [20, 14, 19]
some_list.extend(new_list)
print(some_list[3:5])

#   д) Поміняйте місцями найбільше та найменше число в списку.
max_index = some_list.index(max(some_list))
min_index = some_list.index(min(some_list))

some_list[max_index], some_list[min_index] = some_list[min_index], some_list[max_index]
print(some_list)




# 2.  Tuple (Кортеж):
#     а) Створіть кортеж з трьох різних елементів. Виведіть кортеж на екран.
some_tuple = ('hello', 34, 20)
print(some_tuple)

#     Спробуйте змінити значення першого елемента кортежу.
#     Спостереження: кортежі є незмінними, тому ця спроба має завершитися помилкою.
new_tuple = ('hi', some_tuple[1], some_tuple[2])
print(new_tuple)

#     б) Створіть другий кортеж та об'єднайте два кортежі в один. Виведіть оновлений кортеж.
another_tuple = ( 'nice to meet you', 10, 1)
list_1 = list(some_tuple)
list_2 = list(another_tuple)

new_list = list_1 + list_2
tuple = tuple(new_list)
print(tuple)

# 3.  Set (Множина):
#     а) Створіть множину, яка містить 4 різних значення. Виведіть множину на екран.
some_set = { 'red', 'orange', 'green', 'yellow'}
print(some_set)

#     б) Додайте нове значення до множини. Виведіть оновлену множину.
some_set.add('indigo')
print(some_set)

#     в) Видаліть одне значення з множини. Виведіть оновлену множину.
some_set.remove('red')
print(some_set)

# 4.  Frozenset (Незмінювана множина):
#   а) Створіть frozenset, що містить 3 різних значення. Виведіть frozenset на екран.
frozenset_some_set = frozenset(some_set)
print(frozenset_some_set)

#     б) Спробуйте змінити (додати або видалити) значення в frozenset.
#     Спостереження: frozenset є незмінним, тому будь-яка спроба зміни має завершитися помилкою.

# frozenset_some_set.add('blue')
# print(frozenset_some_set)

#     в) Створіть ще один frozenset з різними значеннями.
#     Об'єднайте два frozenset в новий frozenset. Виведіть отриманий frozenset.
my_set = {'Hi', 'goodbye'}
my_frozenset = frozenset(my_set)
print(my_set)

concatunated_frozenset = frozenset.union(my_frozenset, frozenset_some_set)
print(concatunated_frozenset)
