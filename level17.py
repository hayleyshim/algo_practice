"""
#11047
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다.
(1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

"""
N, K = map(int, input().split())
coin_list = list()

for i in range(N):
    coin_list.append(int(input()))

count = 0

for i in reversed(range(N)):
    count += K//coin_list[i]
    K %= coin_list[i]

    if K == 0:
        break

print(count)