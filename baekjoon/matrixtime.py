arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]


r1, c1 = len(arr1),len(arr1[0])
r2, c2 = len(arr2),len(arr2[0])
answer = [[0 for _ in range(c2)] for _ in range(r1)]
for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            answer[i][j] += arr1[i][k]*arr2[k][j]

print(answer)



#print(len(arr1),len(arr1[0])) 
# arr1 행수 x 열수
# arr2 행수 x 열수
#arr1 1번째 행 x arr2 1번째 열 각각원소 곱해서 더하기