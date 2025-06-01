from itertools import combinations
nan_list = []
for _ in range(9):
    nan_list.append(int(input()))

result = combinations(nan_list, 7)

for combo in result:
    if sum(combo) == 100 :
        combo = sorted(list(combo))
        for c in combo:
            print(c)
        exit()