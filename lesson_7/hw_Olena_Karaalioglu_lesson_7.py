# 1.   Створити функцію, що приймає число з консолі (використати фунцію input());
#   Функція повинна обробити значення таким чином: використовуючи вбудовану функцію int()
#   спробувати конвертувати рядок в число (input() завжди повертає рядок).
#   Якщо конвертувати не виходить, то вивести в консоль "Entered not valid data".

def integer_validation (input_string):
    try:
        integer = int(input_string)
        print('You did it!')
    except ValueError:
        print('Entered not valid data')

user_input = input('Введіть ціле число: ')
integer_validation(user_input)


#2.  Створити функцію, що приймає 2 рядки;
 # Якщо хоча б один рядок не виходить конвертувати в число, тоді робимо конкатенацію (з'єднуємо рядки),
# якщо ж обидва значення можна конвертувати в числа, то отримуємо їх суму. Результат друкуємо в консоль.

def two_strings (string_1, string_2):
    try:
        value_1 = int(string_1)
        value_2 = int(string_2)
        result = value_1 + value_2
        print('Now is the year:', result)
    except ValueError:
        string_value = string_1 + string_2
        print('Summary of strings:', string_value)

user_input_1 = input('Your age: ')
user_input_2 = input('Date of birth: ')
two_strings(user_input_1, user_input_2)

# 3.  Створити функцію, що приймає значення з консолі. Якщо значення не можна привести до числа,
#   тоді просимо користувача ввести інше значення, доки він не введе число. Згадуємо про цикл while.
# Коли користувач вводить число, дякуємо йому )

def integer_input ():
    while True:
        value = input('Please, input some number: ')
        try:
            some_value = int(value)
            print("Thank you for your entered n umber: ", some_value)
            break
        except ValueError:
            print('You entered wrong value. Please, try again: ')

integer_input()


#4.   Створити власне виключення. Наприклад OnlyEvenError. Створити функцію check_digit(), яка приймає число.
  #Якщо число не парне, то породжувати це своє виключення, якщо парне, то повертати його (return)

class OnlyEvenError(Exception):
    pass

def check_digit(number):
    if number % 2 == 0:
        return number
    else:
        raise OnlyEvenError('you entered odd number.')

try:
    value = int(input('Enter even number: '))
    result = check_digit(value)
    print("Your number is even:", result)
except OnlyEvenError as error:
    print('Error: ', str(error))

#5.  Створити функцію, що буде приймати число як аргумент і викликАти в тілі функцію check_digit,
# в яку передавати це число.













