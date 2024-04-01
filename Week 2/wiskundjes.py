def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result
    
def ggd(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        print('Dit is geen geldige invoer. Gaarne gehele positieve getallen.')
    else:
        while(b>0):
            rest=a%b
            a,b=b,rest
        return a

def ggd_rec(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        print('Dit is geen geldige invoer. Gaarne gehele positieve getallen.')
    elif b==0:
        return(a)
    else:
        return ggd_rec(b,a%b)
    
def can_convert_str_to_type(str, type):
    try:
        type(str)
    except:
        return False
    return True
    
def input_int(prompt, min, max):
    i = input(prompt)
    while not can_convert_str_to_type(i, int) or int(i) < min or int(i) > max:
        i = input(prompt)
    return int(i)

def avggr():
    r1 = input_int('Geef eerste resultaat ', 1, 10)
    r2 = input_int('Geef tweede resultaat ', 1, 10)
    print('Het gemiddelde is: ', ((r1+r2)/2))
    
def fact(n):
    num = 1
    while n>=1:
        num=num*n
        n=n-1
    print(num)
    
def forfact(n):
    one = 1
    for i in range(1,n + 1):
        one = one*i
    print(one)

def my_sqrt(a, x):
    while True:
        print(x)
        y = (x+a/x)/2
        if y == x:
            break
        if abs(y-x) < 0.0000000001:
            break
        x = y