# 이차원리스트 : for문 중첩
def solution(row, col):
    result = [[0 for _ in range(col)] for _ in range(row)] #0으로 채워진 2차원 리스트
    num = 1

    for r in range(row):
        for c in range(col):
            result[r][c] = num
            num += 1

    return result


def main():
    r = 5
    c = 5
    ary = solution(r, c)
    print(ary)

if __name__ == "__main__":
    main()



# r = 5, c = 5 인 경우
#  [[1, 6, 11, 16, 21],
#   [2, 7, 12, 17, 22],
#   [3, 8, 13, 18, 23],
#   [4, 9, 14, 19, 24],
#   [5,10, 15, 20, 25]]
