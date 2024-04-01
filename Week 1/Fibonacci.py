def print_rij_van_Fibonacci(n):
    fib0 = 0
    fib1 = 1
    print(0)
    print(1)
    for i in range(n-2):
        fibn=fib0+fib1
        print(fibn)
        fib0 = fib1
        fib1 = fibn