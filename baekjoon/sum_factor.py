def find_factor(N):
    f_list = []
    for i in range(1, N):
        if N%i == 0:
            f_list.append(i)
    return f_list

while True:
    N = int(input())
    if N == -1:
        break
    else :
        f_list = find_factor(N)
        if sum(f_list) == N:
            print(N,"=", 1,end="")
            for i in range(1,len(f_list)):
                print(" +", f_list[i], end="")
            print()
        else :
            print(N,"is","NOT","perfect.")


## gpt 코드

import sys
input = sys.stdin.readline

def proper_divisors(n):
    """n의 자신을 제외한 모든 약수를 오름차순 리스트로 반환"""
    divs = [1]
    # 2부터 √n까지 확인
    limit = int(n**0.5)
    for i in range(2, limit+1):
        if n % i == 0:
            divs.append(i)
            j = n // i
            if j != i:          # 제곱수인 경우 중복 방지
                divs.append(j)
    return sorted(divs)

while True:
    n = int(input())
    if n == -1:
        break

    divs = proper_divisors(n)
    if sum(divs) == n:
        # perfect
        # "6 = 1 + 2 + 3" 형태로 포맷팅
        print(f"{n} = " + " + ".join(map(str, divs)))
    else:
        print(f"{n} is NOT perfect.")