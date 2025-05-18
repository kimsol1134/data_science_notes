n = int(input())
work_list = []
for _ in range(n):
    day, pay = map(int,input().split())
    work_list.append((day,pay))

dp = [0] * 16 # dp 배열 초기화 , 값은 pay 의 최댓값, 인덱스를 날짜로 
# 첫번째 조건 cur_day 값이 n 보다 크면 안됨
# 두번째 조건 cur_pay 최대로 만들기

cur_day = 0
cur_pay = 0
for day,pay in work_list :
    if cur_day + day <= n :
