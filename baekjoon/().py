N = int(input())
for _ in range(N):
    g = input()
    if len(g) % 2 == 1:
        print("NO")
    else :
        score_1 = 0
        score_2 = 0
        
        for i in g:
            if i == "(":
                score_1 +=1
            else :
                score_2 +=1
            if score_2 > score_1:
                print("NO")
                break
        else : #for 루프 내부에서 break가 실행되면 else블록 실행되지 않음

            if score_1 == score_2:
                print("YES")
            else :
                print("NO")    

        