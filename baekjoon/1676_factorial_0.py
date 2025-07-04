n = int(input())

def factorial(n):
    if n ==0:
        return 1
    ans = 1
    for i in range(1,n+1):
        ans=ans*i
    return ans
i = 1
cnt = 0
while 10**i < factorial(n):
    if factorial(n)%(10**i) == 0:
        cnt +=1
        i +=1
    else :
        break
print(cnt)