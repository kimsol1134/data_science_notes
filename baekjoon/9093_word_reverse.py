n = int(input())

for _ in range(n):
    word_list = list(input().split())
    for w in word_list:
        print(w[::-1], end=" ")
