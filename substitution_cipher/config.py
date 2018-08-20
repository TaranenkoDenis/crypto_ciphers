from string import ascii_letters

origin = '{}{}'.format(ascii_letters, '1234567890 `~-=_+/*[]{}|;:/?!.>,<')
reversed_list = ''.join(list(reversed(origin)))
