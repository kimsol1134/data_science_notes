from itertools import product
n, m = map(int, input().split())

num_list = [x for x in range(1, n+1)]

result = list(product(num_list, repeat=m))

for w in result :
    print(*w)