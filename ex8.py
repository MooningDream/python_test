formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, False, True)) # care about the CAP
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    '\n try your\n',
    'own text here\n',
    'maybe a poem\n',
    'or a song about fear\n'
))