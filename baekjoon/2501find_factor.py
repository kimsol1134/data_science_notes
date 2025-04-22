N, K = map(int, input().split())

def find_factor(N):
    num_list = []
    for i in range(1, N+1):
        if N%i == 0:
            num_list.append(i)
    return num_list

num_list = find_factor(N)
if len(num_list) >K:
    print(num_list[K-1])
else :
    print(0)