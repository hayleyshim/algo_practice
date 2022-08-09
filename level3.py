"""#N) 2739

n = int(input())

for i in range(1,10):
    print(n, '*', i, '=', n*i)"""


#N) 10950
t = int(input()) # 테스트 케이스 개수 t를 입력받음

for i in range(t): # t 만큼 반복
    a,b = map(int,input().split()) #split 함수를 이용해서 공백을 기준으로 두 문자열을 분리하고 정수로 변환하기 위해서 map 함수를 이용하여 코드를 한 줄로 작성
    print(a+b)