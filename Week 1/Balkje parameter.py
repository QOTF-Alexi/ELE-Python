def line(width):
    print('-' * width)

def sides(width):
    print('|' + ' ' * (width-2) + '|')

def box(width, height):
    line(width)
    for i in range(height):
        sides(width)
    line(width)
