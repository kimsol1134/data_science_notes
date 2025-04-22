def is_prime(N):
    p_list = [True]*(N+1)
    p_list[0]  = False
    if N >=1:
        p_list[1] = False
    
    for i in range(2, N+1):
        if p_list[i] == True:
            for j in range(i*i, N+1, i):
                p_list[j] = False
    return [i for i in range(2,N+1) if p_list[i]]

M = int(input())
N = int(input())

M_list = is_prime(M-1)
N_list = is_prime(N)

result = [x for x in N_list if x not in M_list]
if result ==[]:
    print(-1)
else :
    print(sum(result))
    print(result[0])