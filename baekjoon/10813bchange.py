N , M = map(int,input().split())

b_list = []
for i in range(N):
    b_list.append(i+1)
    
for _ in range(M):
    i,j =map(int,input().split())
    b_list[i-1],b_list[j-1] = b_list[j-1], b_list[i-1]
print(*b_list)