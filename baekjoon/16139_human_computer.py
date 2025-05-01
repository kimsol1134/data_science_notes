word = list(input())
n = int(input())
for _ in range(n):
    a,l,r = input().split()
    l = int(l)
    r = int(r)
    print(word[l:r+1].count(a))