print('문자입력')
char = input()
print('문자:\n', char)

print('숫자입력')
num = int(input())
print('숫자:\n',num)

print('실수입력')
f = float(input())
print('실수:\n',f)

print('첫번째 문자 입력\n')
a = input()

print('두번째 문자 입력')
b = input()
print(a + '\n' + b)

print('첫번째 문자 입력\n')
a = input()

print('두번째 문자 입력')
b = input()
print(b + '\n' + a)

print('실수 입력\n')
f = input()
print(f + '\n' + f + '\n' + f)

print('정수 2개 입력 후 그대로 출력\n')
a, b = input().split()
print(a + '\n' + b)

print('문자 2개 입력 후 바꿔서 출력\n')
a, b = input().split()
print(b + '\n' + a)

str = input()
print(str, str, str)

h, m = input().split(':')
print(h, m, sep=':')