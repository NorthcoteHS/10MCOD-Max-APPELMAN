"""
basically a lot of stuff from the internet all joined together
"""

#the ascii stuff
from string import ascii_letters

#makes the letters shift
cipher_letters = 'bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA'


def cipher(text):
    trans = str.maketrans(ascii_letters, cipher_letters)
    return text.translate(trans)


if __name__ == '__main__':
    message = input('Write a message: ')
    ciphered = cipher(message)

    print(f'Ciphered text: {ciphered}')
