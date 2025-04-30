words_list=list(input().split("-"))

ans=""

for word in words_list:
    ans+=word[0]

print(ans)