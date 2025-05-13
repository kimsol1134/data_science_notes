import sys
input = sys.stdin.readline

def prime_list(n):
    p_list = [True] * (n+1)
    p_list[0] = p_list[1] = False

    for i in range(2,int(n**0.5)+1):
        if p_list[i] == True:
            for j in range(i*i, n+1, i):
                p_list[j] = False
    return [i for i in range(2, n+1) if p_list[i]]

prime_list = prime_list(1000001)
prime_set = set(prime_list[1:])  #집합으로 하면 in 연산 O(1)
prime_list = prime_list[1:]

while True:
    n = int(input())
    if n == 0 :
        break
    for i in prime_list:
        if i > n:
            break
        if n - i in prime_set:
            print(f"{n} = {i} + {n-i}")
            break
    else:
        print("Goldbach's conjecture is wrong")