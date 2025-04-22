mat = [[-1 for _ in range(15)] for _ in range(5)] # 15x5 기본행렬 생성

for i in range(5):
    word = input()
    for j, w in enumerate(word):
        mat[i][j] = w

new_word = ""
for i in range(15):
    for j in range(5):
        if mat[j][i] != -1:
            new_word += mat[j][i]
print(new_word)

