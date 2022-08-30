"""
#1780
첫째 줄에 N(1 ≤ N ≤ 37, N은 3k 꼴)이 주어진다. 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.
첫째 줄에 -1로만 채워진 종이의 개수를,
둘째 줄에 0으로만 채워진 종이의 개수를,
셋째 줄에 1로만 채워진 종이의 개수를 출력한다.
분할정복
"""
import sys
#input = sys.stdin.readline()

#입력 받기
n = int(input())
minus_cnt, zero_cnt, plus_cnt = 0, 0, 0

papers = []
for _ in range(n):
    row = list(map(int, input().rsplit()))
    papers.append(row)

#현재 종이 색상과 다르면 분할하기

def check(row, col, n):
    global minus_cnt, zero_cnt, plus_cnt
    #현재 종이 색상
    curr = papers[row][col]

    for i in range(row, row + n):
        for j in range(col, col + n):
            if papers[i][j] != curr:
                # 다음 종이의 길이는 1/3
                next_n = n // 3
                check(row, col, next_n)  # 1
                check(row, col + next_n, next_n)  # 2
                check(row, col + (2 * next_n), next_n)  # 3
                check(row + next_n, col, next_n)  # 4
                check(row + next_n, col + next_n, next_n)  # 5
                check(row + next_n, col + (2 * next_n), next_n)  # 6
                check(row + (2 * next_n), col, next_n)  # 7
                check(row + (2 * next_n), col + next_n, next_n)  # 8
                check(row + (2 * next_n), col + (2 * next_n), next_n)  # 9
                return

    # 현재 종이 색상에 따라 갯수 세기
    if curr == -1:
        minus_cnt += 1
    elif curr == 0:
        zero_cnt += 1
    elif curr == 1:
        plus_cnt += 1
    return

check(0, 0, n)

print(minus_cnt)
print(zero_cnt)
print(plus_cnt)