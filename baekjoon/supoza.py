def pattern(list,n):
    patterns = (list * (n//len(list)+1))
    patterns = patterns[:n]
    return patterns

def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    one_list = pattern(one,len(answers))
    two_list = pattern(two,len(answers))
    three_list = pattern(three,len(answers))t
    two_scores = 0
    three_scores = 0
    
    for i in range(len(answers)):
        if answers[i] == one_list[i]:
            one_scores +=1
        if answers[i] == two_list[i]:
            two_scores +=1
        if answers[i] == three_list[i]:
            three_scores +=1
            
    answer = []
    if one_scores == max(one_scores,two_scores,three_scores):
        answer.append(1)
    if two_scores == max(one_scores,two_scores,three_scores):
        answer.append(2)
    if three_scores == max(one_scores,two_scores,three_scores):
        answer.append(3)
        
    print(answer)
    return answer




'''
1번 찍는 방법 :1,2,3,4,5 반복
2번 찍는 방법 :2,1,2,3,2,4,2,5,2,1,2,3,2,4,2,5반복
3번 찍는 방법 :3,3,1,1,2,2,4,4,5,5 반복

1번의 정답 리스트 만들기 5로 나눈 나머지, 0이면 5?
2번의 정답 리스트 만들기 홀수일때 2 짝수일때는 1,3,4,5 
3번의 정답 리스트 만들기

정래진 리스트를 순서대로 넣어주는 방법 없나?

정답표랑 정답비교해서 갯수 세기

return 값 가장 많은 문제를 맞힌 사람 번호 배열에 오름차순으로 담아

'''
print(solution([1,2,3,4,5]))
