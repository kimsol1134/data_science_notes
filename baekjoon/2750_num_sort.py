n = int(input())
ans = []
for _ in range(n):
    i = int(input())
    ans.append(i)
ans_sort = sorted(ans)
for w in ans_sort:
    print(w)    