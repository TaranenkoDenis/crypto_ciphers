import config


def cipher(input_str, key):
    check_key(key)

    result_data = []

    for ch in input_str:
        try:
            is_title = ch.istitle()
            index = config.eng_alphabet.index(
                ch if not is_title else ch.lower()
            )

            new_index = index + key

            if (new_index > config.len_eng_alphabet):
                new_index = new_index - config.len_eng_alphabet

            new_char = config.eng_alphabet[new_index]

            if is_title and not new_char.istitle():
                new_char = new_char.upper()

            result_data.append(new_char)

        except ValueError:
            result_data.append(ch)

    return ''.join(result_data)


def decipher(_str, key):
    check_key(key)

    result_data = []

    for ch in _str:
        try:
            is_title = ch.istitle()
            index = config.eng_alphabet.index(
                ch if not is_title else ch.lower()
            )

            new_index = index - key

            if (new_index < 0):
                new_index = config.len_eng_alphabet + new_index

            new_char = config.eng_alphabet[new_index]

            if is_title and not new_char.istitle():
                new_char = new_char.upper()

            result_data.append(new_char)

        except ValueError:
            result_data.append(ch)

    return ''.join(result_data)


def check_key(key):
    if not isinstance(key, int):
        raise RuntimeError(
            'Not valid key! type of key = {}'.format(str(type(key)))
        )
