"""a = int(input())
result = 0

for i in range(0, a+1, 2):
    result += i
print(result)

"""

"""i, result = 2, 0
a = int(input())
while (i <=a):
    result += i
    i += 2
print(result)"""

"""a = int(input())
result = 0
for i in range(a+1):
    if i%2 == 0:
        result += i
print(result)"""

"""a = ' '
while(a!='q'):
    a = input()
    print(a)
"""

"""while(1):
    a = input()
    print(a)
    if a== 'q' : break"""

"""a = int(input())
n = 0
for i in range(1,a):
    n += i
    if (n>=a):
        print(i)
        break"""

"""a = int(input())
n =0
for i in range(1,a):
    n += i
    if(n>=a):
        print(i)
        break"""
"""
a = int(input())
n = 0
if a<3: print(a)
for i in range(1,a):
    n += i
    if(n >= a):
        print(i)
        break"""

"""a, b = map(int, input().split())
for x in range(1, a+1):
    for y in range(1, b+1):
        print(x,y)
"""

"""a, b = map(int, input().split())
for i in range(a):
    for j in range(b):
        print(i+1, j+1)"""

"""a = int(input(), 16)
for i in range(1, 16):
    print('%X*%X=%X' %(a,i,a*i))
"""
"""
h, b, c, s = map(int, input().split())
print('%.1f'%(h*b*c*s/8/1024/1024), 'MB')"""
"""
w, h, b = map(int, input().split())
print('%.2f' %(w*h*b/8/1024/1024), 'MB')"""

"""a = int(input())

result = 0
for i in range(a+1):
    if result >= a:
        break
    result += i

print(a if a < 3 else result)"""

"""a = int(input())

for i in range(1, a+1):
    if i % 3 != 0:
        print(i, end =' ')"""

"""a, d, n = map(int, input().split())
result = a
for i in range(n-1):
    result += d
print(result)"""

"""a, r, n = map(int, input().split())
result = a
for i in range(n-1):
    result *= r
print(result)
"""

"""a, m, d, n = map(int, input().split())
for i in range(1, n):
    a = a*m+d

print(a)"""

"""a, b, c = map(int, input().split())
d = 2
while d%a!=0 or d%b!=0 or d%c!=0:
    d += 1
print(d)"""

"""num = int(input())
a = list(map(int, input().split()))
student = [0]*23
for i in a:
    student[i-1] += 1
print(" ".join(repr(i) for i in student))"""

"""num = int(input())
a = list(map(int, input().split()))
print(" ".join(repr(i for i in reversed(a))))
"""
"""num = int(input())
a = list(map(str, input().split()))
print(' '.join(reversed(a)))"""

"""num = int(input())
a = list(map(int, input().split()))
a.sort()
print(a[0])"""

