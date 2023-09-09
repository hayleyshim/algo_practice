a, b = map(int, input().split())
print(a if (a>b) else b)

a, b, c = map(int, input().split())
print(a if a < b and a < c else b if b < c else c)

a, b, c = map(int, input().split())
x = a if a < b else b
y = x if x < c else c
print(y)