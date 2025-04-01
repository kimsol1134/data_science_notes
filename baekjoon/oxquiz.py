
n = int(input())

for _ in range(n):
    score =0
    ans = input()
    ans = ans.split("X")
    for i in ans :
        if i !='':
            for j in range(1,len(i)+1):
                score+=j 
    print(score)
'''
문제수 0~80
연속된 O의 값이 점수

X가 있으면 다시 0 점부터 시작


'''