
# n, m = map(int,input().split())

# def factorial(n):
#     if n ==0:
#         return 1
#     ans = 1
#     for i in range(1,n+1):
#         ans=ans*i
#     return ans

# i = 1
# cnt = 0
# def combination(n,m):
#     return factorial(n)/(factorial(n-m)*factorial(m))

# combination = combination(n,m)
# while 10**i < combination:
#     if combination%(10**i) == 0:
#         cnt +=1
#         i +=1
#     else :
#         break
# print(cnt)


import math
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
comb = math.comb(n,m)

i = 1
cnt = 0
while 10**i < comb:
    if comb%(10**i) == 0 :
        cnt +=1
        i+=1
    else :
        break
print(comb)