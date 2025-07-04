N , M = map(int,input().split())

b_list = [0] * N
for _ in range(M):
    i,j,k =map(int,input().split())
    for l in range(i,j+1):
        b_list[l-1] = k
print(*b_list)