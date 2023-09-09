"""n = int(input())
print(bool(n))
"""

"""a = bool(int(input()))
print(not a)
"""

a, b = map(int, input().split())
print(bool(a) and bool(b))

a, b = map(int, input().split())
print(bool(a) or bool(b))

a, b = map(int, input().split())
print(bool(a) != bool(b))

a, b = map(int, input().split())
print(bool(a) == bool(b))

a, b = map(int, input().split())
print(bool(a) == bool(b) == False)