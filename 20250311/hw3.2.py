reversed('parrot')
print(reversed('parrot'))

list(reversed('parrot'))
print(list(reversed('parrot')))

''.join(reversed('parrot'))
print(''.join(reversed('parrot')))

def reverse_word(word):
    return ''.join(reversed(word))

def is_palindrome(word):
    return word == reverse_word(word)

word_list = ['noon', 'redivider', 'deified', 'civic', 'radar', 'level', 'rotor', 'kayak', 'reviver', 'racecar', 'madam', 'refer']   

for word in word_list:
    if len(word) >= 7 and is_palindrome(word):
        print(word)