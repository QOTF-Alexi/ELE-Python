from math import sqrt
def print_roots(a, b, c):
    if (b**2)-4*a*c < 0:
        print('Deze vierkantswortel heeft geen reele wortels.')
    else:
        if (b**2)-4*a*c == 0:
            oneRoot = (-b+sqrt((b**2)-4*a*c))/(2*a)
            print('Deze vierkantswortel heeft een reele wortel:', oneRoot)
        else:
            twoRoots1 = (-b+sqrt((b**2)-4*a*c))/(2*a)
            twoRoots2 = (-b-sqrt((b**2)-4*a*c))/(2*a)
            print('Deze vierkantswortel heeft twee reele wortels:', twoRoots1, '&', twoRoots2)