from math import floor
import string
def is_palindrome(text):
    n = len(text)
    half = floor(n/2)
    for i in range(half):
        if text[i] == text[n-1-i]:
            print('A frase: ' + text + ' eh palindromo')
            return 
    print('A frase: ' + text + ' nao eh um palindromo')
    return

is_palindrome('arara')
is_palindrome('palindromo')