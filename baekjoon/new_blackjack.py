N , M = map(int,input().split())
num = list(map(int, input().split()))
num.sort(reverse=True)
answer=[]
for i in range(len(num)) :
    for j in range(i+1,len(num)) :
        for k in range(j+1,len(num)):
            if num[i]+num[j]+num[k] <=M:
                answer.append(num[i]+num[j]+num[k])

print(max(answer))