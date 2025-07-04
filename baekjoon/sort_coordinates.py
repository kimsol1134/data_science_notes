N = int(input())
list = []
for _ in range(N):
    a , b = map(int, input().split())
    list.append((a,b))
list.sort(key=lambda x : (x[0], x[1]))

for w in list:
    print(w[0],w[1])