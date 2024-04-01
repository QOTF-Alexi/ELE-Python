def boxed(s):
    lines = '+' + '-' * (len(s)+4) + '+'
    print(lines)
    print('|  ' + s + '  |')
    print(lines)