import sys
input = sys.stdin.readline

n, m = map(int,input().split())

def num_zero(n):
    """
    n! (n 팩토리얼)의 끝에 있는 0의 개수를 계산합니다.

    매개변수:
    n (int): 0 이상 500 이하의 정수

    반환값:
    int: n!의 끝에 있는 0의 개수
    """
    if n < 0:
        # 문제 조건은 0 이상이지만, 예외 처리
        return "음수는 팩토리얼을 계산할 수 없습니다."
    if n == 0:
        return 0

    count = 0
    i = 5
    while (n // i) >= 1:
        count += (n // i)
        # 다음 5의 거듭제곱으로 넘어갈 때 오버플로우를 방지하기 위해
        # i가 너무 커지지 않도록 확인합니다. (N <= 500 이므로 사실상 불필요)
        if i > n / 5: # i * 5가 n을 넘어가면 더 이상 진행할 필요 없음
            break
        i *= 5
    return count
if num_zero(n)-num_zero(n-m)-num_zero(m) <= 0 :
    print(0)
else :
    print(num_zero(n)-num_zero(n-m)-num_zero(m))

import math
print(math.comb(n , m))
print(num_zero(n)-num_zero(n-m)-num_zero(m))
