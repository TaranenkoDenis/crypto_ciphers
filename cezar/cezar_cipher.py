from string import ascii_letters

l = '{}{}'.format(ascii_letters, r'1234567890 `~-=_+/*[]{}|;:/?.>,<\\\'\"')


def cipher(msg, key):
    assert isinstance(key, int)
    return ''.join([l[(l.index(c) + key) % len(l)] for c in msg if c in l])


def decipher(msg, key):
    assert isinstance(key, int)
    return ''.join([l[(l.index(c) - key) % len(l)] for c in msg if c in l])
