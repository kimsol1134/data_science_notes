N, K = map(int,(input().split()))

c_list = []
for i in range(N):
    coin = int(input())
    c_list.append(coin)
c_list.sort(reverse=True)

cnt = 0

for c in c_list:
    if K // c != 0:
        cnt += (K//c)
        K = K - c*(K//c)
print(cnt)