"""
#15596
정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성
def solve(a: list) -> int
- a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
- 리턴값: a에 포함되어 있는 정수 n개의 합 (정수)"""

def solve(a):

    ans = 0
    for x in a:
        ans += x
    return ans

#4673
"""
양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자
n을 d(n)의 생성자라고 한다.

10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
"""

def d(n):
    # int로 들어온 n을 형변환 시켜부면 문자열,
    # 즉. iterable 되고 map 함수를 이용해 int로 바꾸면 각 자리 합 구할 수 있음
    n = n + sum(map(int, str(n)))
    return n

nonSelfNum = set()

for i in range(1, 10001):
    nonSelfNum.add(d(i))

for j in range(1, 10001):
    if j not in nonSelfNum:
        print(j)
