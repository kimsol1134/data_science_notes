matr = []
for i in range(9):
    row = [int(v) for v in input().split()]
    matr.append(row)

max_l = []
for i_ro,ro in enumerate(matr) :
    max_l.append((max(ro),i_ro,ro.index(max(ro))))

ans = max(max_l)
ss = [ans[1]+1,ans[2]+1]
print(ans[0])
print(*ss)



### 효율적인 방법

max_value = -1 # 나올수 없는 값으로 초기화 (문제에서 0이상의 자연수 조건)
max_row = 0
max_col = 0

for r in range(9):
    row_values = list(map(int,input().split()))
    for c in range(9):
        if row_values[c] > max_value: #현재 값이 기존 최댓값보다 크면
            max_value = row_values[c] #최댓값 없데이트
            max_row = r
            max_col = c #최댓값의 행,열값도 업데이트
print(max_value)
print(max_row +1, max_col +1)