# 이차원리스트 : for문 중첩
def solution(row, col):
    result = [[0 for _ in range(col)] for _ in range(row)] #0으로 채워진 2차원 리스트
    num = 1

    for r in range(row):
        if r % 2 == 0:
            for c in range(col):
                result[r][c] = num
                num += 1

        else:
            for c in range(col-1, -1, -1):
                result[r][c] = num
                num+=1

    return result


def main():
    r = 5
    c = 5
    ary = solution(r, c)
    print(ary)

if __name__ == "__main__":
    main()

# r = 5, c = 5 인 경우
# [[ 1, 2, 3, 4, 5],
#  [10, 9, 8, 7, 6],
#  [11,12,13,14,15],
#  [20,19,18,17,16],
#  [21,22,23,24,25]]
