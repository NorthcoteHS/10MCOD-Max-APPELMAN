"""""""""
something
"""
pig = 'ay'
original = input('Enter a word and magic will happen: ')


while original:
        word = original.lower()
        first = word[0]
        if original==('no'or'nop'or'nope'):
                print('just go')
        elif first == ('a' or 'e' or 'i' or 'o' or 'u'):
            new_word = word + pig
            print (new_word)
            original = input('Enter a word and magic will happen: ')
        else:
            new_word = word[1:] + first + pig
            print (new_word)
            original = input('Enter a word and magic will happen: ')
            
print('well you suck')
agic=input('ENTER A PROPER WORD THIS TIME! ')
if agic:
    print('Thank you for choosing '+agic+', have a great day and go away')
else:
    print('You REALLY suck, bye now')

