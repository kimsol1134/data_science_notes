from itertools import combinations_with_replacement
n, m = map(int, input().split())

num_list = [x for x in range(1, n+1)]

result = list(combinations_with_replacement(num_list, m))

for w in result :
    print(*w)