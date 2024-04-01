from math import sqrt
def print_roots(a, b, c):
    det = (b**2)-4*a*c
    posSqrt = (-b+sqrt(det))/(2*a)
    if det < 0:
        print('Deze vierkantswortel heeft geen reele wortels.')
    elif det == 0:
        oneRoot = posSqrt
        print('Deze vierkantswortel heeft een reele wortel:', posSqrt)
    else:
        twoRoots2 = (-b-sqrt(det))/(2*a)
        print('Deze vierkantswortel heeft twee reele wortels:', posSqrt, '&', twoRoots2)