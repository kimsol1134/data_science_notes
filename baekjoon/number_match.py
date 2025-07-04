def solution(X, Y):
    X_list = list(X)
    Y_list = list(Y)
    
    m_list = []
    answer = []
    for i in range(10):
        m_list.append(min(X_list.count(str(i)),Y_list.count(str(i))))
    
    for i in range(10):
        if m_list == [0,0,0,0,0,0,0,0,0,0]:
            answer = "-1"
            return answer
        else :
            answer.append(m_list[i]*str(i))
    
    if answer.count('')==9 and set(list(answer[0])) == {'0'}:
        answer ="0"
        return answer
    
    else:
        answer.sort(reverse=True)
        answer =''.join(answer)
        return answer


'''
3 ≤ X, Y의 길이(자릿수) ≤ 3,000,000입니다.
답은 문자열로 반환
짝이 없으면 -1

리스트로 변환 

짝 이라는거는 같은 숫자가 다른 자릿수에 있어도 됨
count()로 각 숫자세서 넣기

내림차순으로 한다음 문자로 반환
'''
print(solution("100" ,"123450"))