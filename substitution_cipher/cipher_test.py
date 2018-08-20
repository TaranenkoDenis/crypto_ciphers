import substitution_cipher


def run_test():
    str_for_encryption = input(
        'Input string on english language for encription: ')

    cyphered_str = substitution_cipher.cipher(str_for_encryption)
    print('cyphered_str = %s' % cyphered_str)

    decyphered_str = substitution_cipher.decipher(cyphered_str)
    print('decyphered_str = %s' % decyphered_str)


if __name__ == '__main__':
    run_test()
