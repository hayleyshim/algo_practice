def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r

    return a


def lcm(a, b):
    return a * b // gcd(a, b)


arr = [10, 30, 20, 10]


answer = gcd(arr[0], arr[1])
for i in range(2, len(arr)):
    answer = gcd(answer, arr[i])
print(answer)

arr = [25, 40, 60]
answer = gcd(arr[0], arr[1])
for i in range(2, len(arr)):
    answer = gcd(answer, arr[i])
print(answer)

arr = [15, 55, 20, 30, 40]
answer = gcd(arr[0], arr[1])
for i in range(2, len(arr)):
    answer = gcd(answer, arr[i])
print(answer)