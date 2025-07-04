'''
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
시간제한 2초
'''

M, N = map(int, input().split())

def is_prime(M,N):
    p_list = [True]*(N+1)
    p_list[0] = p_list[1] = False
    for i in range(2,int(N**0.5)+1):
        if p_list[i]:
            for j in range(2*i,N+1, i): # for j in range(i*i, N+1, 1)
                p_list[j] = False
    return [i for i in range(M, N+1) if p_list[i]]

for a in is_prime(M,N) :
    print(a)



def is_prime(N):
    p_list = [True] * (N+1)
    p_list[0] = p_list[1] = False #0,1은 소수아님

    for i in range(2, N+1):
        if p_list[i] == True:
            for j in range(i*i, N+1, i): #i의 배수들은 다 소수 아님
                p_list[j] = False
    return [i for i in range(2, N+1) if p_list[i]] #p_list의 True면 리스트에 추가

