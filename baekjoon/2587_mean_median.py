num_list = []
for _ in range(5):
    n = int(input())
    num_list.append(n)
print(int(sum(num_list)/len(num_list)))
num_list = sorted(num_list)
print(num_list[2])