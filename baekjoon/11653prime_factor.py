import sys

input = sys.stdin.readline
print = sys.stdout.write

def is_prime(N):
    p_list = [True] * (N+1)
    if N == 1 :
        return
    p_list[0] = p_list[1] =False
    
    for i in range(2, int(N**0.5)+1):
        if p_list[i] == True:
            for j in range(i*i, N+1, i):
                p_list[j] = False
    return [i for i in range(2,N+1) if p_list[i]]

N = int(input())
if N == 1 :
    pass
else :
    p_list = is_prime(N)

    f_list = []
    for p in p_list :
        while True:
            if N % p == 0:
                f_list.append(str(p) + '\n')
                N = N//p
            else :
                break
    for f in f_list:
        print(f)
