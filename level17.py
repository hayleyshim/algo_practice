"""
#11047
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다.
(1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

그리디 알고리즘 : 미래를 생각하지 않고 각 단계에서 가장 최선의 선택을 하는 기법

"""
N, K = map(int, input().split())

coin = []
cnt = 0

for i in range(N) :
    coin.insert(0, int(input()))

for i in coin :
    cnt += K // i #몫을 cnt에 더함
    K = K % i #나머지로 확인

print(cnt)