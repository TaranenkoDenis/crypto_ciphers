import config

orign = config.origin
revers = config.reversed_list


def cipher(msg):
    return ''.join([revers[orign.index(c)] for c in msg if c in msg])


def decipher(msg):
    return ''.join([orign[revers.index(c)] for c in msg if c in msg])
