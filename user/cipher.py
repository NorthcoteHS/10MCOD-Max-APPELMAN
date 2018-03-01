from string import ascii_letters

cipher_letters = 'nzghqkcdmyfoialxevtswrupjbNZGHQKCDMYFOIALXEVTSWRUPJB'


def lol_cipher(text):
    trans = str.maketrans(ascii_letters, cipher_letters)
    return text.translate(trans)

if __name__ == '__main__':
    texto = input('Write something: ')
    ciphered = lol_cipher(texto)

    print(f'Ciphered text: {ciphered}')
    
