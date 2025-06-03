from itertools import combinations
n, m = map(int, input().split())

num_list = [x for x in range(1, n+1)]

result = list(combinations(num_list, m))

for w in result :
    print(*w)