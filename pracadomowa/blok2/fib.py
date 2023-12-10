def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for x in range(2, n + 1):
            a, b = b, a + b
        return b

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(10))
print(fib(1000))

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...


#0,1,2,3,4,5,6,7,8,910
#0 1 1 2 3 5 8 13 21 34 55