from string import ascii_letters
from itertools import cycle

alph = '{}{}'.format(ascii_letters, r'1234567890 `~-=_+/*[]{}|;:/?!.>,<')


def cipher(msg, key):
    keys = formatKey(key)
    gen = createGeneratorKeys(keys)

    return ''.join(
        [alph[((alph.index(c) + next(gen)) % len(alph))]
         for c in msg if c in alph]
    )


def decipher(msg, key):
    keys = formatKey(key)
    gen = createGeneratorKeys(keys)

    return ''.join(
        [alph[((alph.index(c) - next(gen)) % len(alph))]
         for c in msg if c in alph]
    )


def formatKey(key):
    assert isinstance(key, int)
    return [int(i) for i in str(key)]


def createGeneratorKeys(keys):
    for k in cycle(keys):
        yield k
