def fib(n):
    num1 = 0
    num2 = 1
    if n == 0:
        return num1
    if n == 1:
        return num2

    for _ in range(2, n+1):
        summ = num1 + num2
        num1 = num2
        num2 = summ

    return num2

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
