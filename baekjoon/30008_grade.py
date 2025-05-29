n, k = map(int, input().split())
score = list(map(int,input().split()))
grade_list = []

for i in range(k):
    grade = (score[i]*100)//n
    if 0 <= grade <= 4 :
        grade_list.append(1)
    elif 4< grade <= 11 :
        grade_list.append(2)
    elif 11< grade <= 23 :
        grade_list.append(3)
    elif 23 < grade <=40 :
        grade_list.append(4)
    elif 40 < grade <= 60 :
        grade_list.append(5)
    elif 60 < grade <= 77 :
        grade_list.append(6)
    elif 77 < grade <= 89 :
        grade_list.append(7)
    elif 89 < grade <= 96 :
        grade_list.append(8)
    else :
        grade_list.append(9)        

print(*grade_list)