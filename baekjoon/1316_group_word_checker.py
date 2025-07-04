n = int(input())
cnt = 0
    #알파벳 앞부터 세면서 처음 나오는 알파벳 체크
    #두번이상 나오는 알파벳이면 바로 앞 알파벳과 같으면 통과
    # 바로 앞 알파벳과 다르면 그룹단어 아님
for _ in range(n):
    c_list = []
    is_group = True
    word = input()
    for w in word:
        if w not in c_list :
            c_list.append(w)
        else :
            if c_list[-1] == w:
                c_list.append(w)
            else :
                is_group = False
                break
    if is_group== True:
        cnt +=1
print(cnt)