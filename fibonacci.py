def fibonacci(n):
    a, b = 0,1
    for i in range(n):
        a , b = b , a + b  # sequential assignment
    return a

print(fibonacci(3000))


def fibonacci2(n):
    if n <= 1:
        return n
    else: 
        return (fibonacci2(n-1) + fibonacci2(n-2))

print(fibonacci2(3000))

# maximum recursion depth is exceeded