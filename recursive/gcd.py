def gcd(first, second):
    print(first, second)
    if first == second:
        return first
    elif first > second:
        return gcd(first-second, second)
    return 1

print(gcd(196, 42))