N, M = map(int,input().split()) # N x M 행렬
matrix_1 = []
matrix_2 = []
for i in range(N):
    row = [int(v) for v in input().split()]
    matrix_1.append(row)

for i in range(N):
    row = [int(v) for v in input().split()]
    matrix_2.append(row)

for i in range(N):
    for j in range(M):
        print(matrix_1[i][j]+matrix_2[i][j], end=" ")
    print()
