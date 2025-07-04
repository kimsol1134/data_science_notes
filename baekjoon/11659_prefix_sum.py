import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a_list = [int(v) for v in input().split()]
p_sum = [0] * (n+1)

for i in range(1, n+1):
    p_sum[i] = p_sum[i-1] + a_list[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(p_sum[j]-p_sum[i-1])
