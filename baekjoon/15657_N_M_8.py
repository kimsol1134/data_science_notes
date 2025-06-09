from itertools import combinations_with_replacement
n, m = map(int, input().split())

num_list = [int(x) for x in input().split()]
num_list = sorted(num_list)
result = list(combinations_with_replacement(num_list, m))

for w in result :
    print(*w)