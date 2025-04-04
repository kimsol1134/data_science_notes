N , M = map(int,input().split())
num = list(map(int, input().split()))
num.sort(reverse=True)
answer=[]
i = 0
j = 1
k = 2
while num[i]+num[j]+num[k] > M:
    answer.append(num[i]+num[j]+num[k])


answer.sort()
print(answer[-1])