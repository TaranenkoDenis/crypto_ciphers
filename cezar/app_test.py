import cezar_cipher


def run_app():
    str_for_encryption = input(
        'Input string on english language for encription: ')
    int_key = int(input('Input key (integer number from 1 to 90): '))

    cyphered_str = cezar_cipher.cipher(str_for_encryption, int_key)

    print('cyphered_str = %s' % cyphered_str)

    decyphered_str = cezar_cipher.decipher(cyphered_str, int_key)

    print('decyphered_str = %s' % decyphered_str)


if __name__ == '__main__':
    run_app()
