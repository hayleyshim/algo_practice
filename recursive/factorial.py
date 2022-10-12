def factorial(n):
    result = 1

    for i in range(n, 0, -1):
        print(i)
        result *= i
    return result

print(factorial(4))


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

result = factorial(4)
print(result)