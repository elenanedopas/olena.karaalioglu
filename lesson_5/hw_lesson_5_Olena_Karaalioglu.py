# №1-варіант_1
sentence = 'Мені дуже подобається вивчати пайтон! ' \
           'Здається, це найлегша з потужних мов для вивчення'
print(sentence.split())

# №1-варіант_2
sentence_2 = ['Мені дуже подобається вивчати пайтон! '
              'Здається, це найлегша з потужних мов для вивчення']
print(sentence_2[0].split())


# №2 option 1
new_sentence = sentence.replace('е', '#').replace('і', '#').replace('о','#').replace('а','#')\
    .replace('у','#').replace('и','#')

print(sentence)
print(new_sentence)

# №2 option 2
sentence = 'Мені дуже подобається вивчати пайтон! ' \
           'Здається, це найлегша з потужних мов для вивчення'
vowel_in_sentence = 'аоуеіиАОУЕИІ'
for char in sentence:
    if char in vowel_in_sentence:
        sentence = sentence.replace(char, '#')
print(sentence)







