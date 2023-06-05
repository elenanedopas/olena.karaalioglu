# print(1 + 1)
# print('1' + '1')
# age = 23
# print('Jack is ' + str(age) + ' years old.')
# print('Jack is ' + str(23) + ' years old.')

name = 'Jack'
age = 23
name_and_age = 'My name is {0}. I\'m {1} years old.'.format(name, age)
print(name_and_age)
name_and_age = 'My name is {0}. I\'m {1} years old.'.format('Jack', 23)
print(name_and_age)
name_and_age = 'My name is {}. I\'m {} years old.'.format(23, 'Jack')
print(name_and_age)
week_days = 'There are 7 days in a week: {5}, {0}, {3}, {1}, {2}, {4}, {6}.'\
    .format('Monday', 'Wednesday', 'Thursday','Tuesday', 'Friday', 'Sunday',
            'Saturday')
print(week_days)
week_days = 'There are 7 days in a week: {su}, {mo}, {tu}, {we}, {th},' \
           ' {fr}, {sa}.' \
    .format(mo = 'Monday', we = 'Wednesday', th = 'Thursday',
            tu = 'Tuesday', fr = 'Friday', su = 'Sunday',
           sa = 'Saturday')
print(week_days)
week_days = 'There are 7 days in a week: {su}, {su}, {su}, {su}, {su},' ' {su}, {su}.' \
   .format(mo = 'Monday', we = 'Wednesday', th = 'Thursday',
          tu = 'Tuesday', fr = 'Friday', su = 'Sunday',    sa = 'Saturday')
print(week_days)

greeting = 'Hi pretty'
first_name = 'Jessika'
last_name = 'Park'
exclamation_point = '!'
white_space = ' '
coma = ',\n'
whole_sentence = greeting + coma + white_space + \
                 first_name + white_space + last_name + exclamation_point
print(whole_sentence)

#Escaping \
who_am_i = "I'm developer"
print(who_am_i)
who_am_i_2 = 'I want to learn "Python"'
print(who_am_i_2)
who_am_i_3 = "also I want to learn \"Java\""
print(who_am_i_3)


