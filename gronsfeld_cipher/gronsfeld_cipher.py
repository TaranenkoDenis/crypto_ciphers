from string import ascii_letters
from itertools import cycle

alph = string.printable


def cipher(msg, key):
    gen = cycle(map(int, str(key)))
    return ''.join(
        [alph[((alph.index(c) + next(gen)) % len(alph))]
         for c in msg if c in alph]
    )


def decipher(msg, key):
    gen = cycle(map(int, str(key)))
    return ''.join(
        [alph[((alph.index(c) - next(gen)) % len(alph))]
         for c in msg if c in alph]
    )
