"""
#1085
한수는 지금 (x, y)에 있다.
직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다.
직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

"""

x,y,w,h = map(int, input().split())

print(min(x, y, w-x, h-y))


#3009
"""
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성
"""

x_ = []
y_ = []

for i in range(3):
    x,y = map(int, input().split())
    x_.append(x)
    y_.append(y)

#for문이 반복되는 동안 count 함수를 이용해서
# 두 개의 리스트에서 각 인덱스에 위치한 요소의 개수가 한 개인지를 찾았다.
# if조건식으로 두 개의 리스트에서 count 개수가 1인 요소를 각각 x4, y4 변수에 선언하여 출력하였다.


for i in range(3):
    if x_.count(x_[i]) == 1:
        x = x_[i]
    if y_.count(y_[i]) == 1:
        y = y_[i]

print(x,y)