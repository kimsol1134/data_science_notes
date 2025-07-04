# n = int(input())

# num_list = [0] * (1001)
# num_list[1] = 1
# num_list[2] = 2
# for i in range(3, n+1):
#     num_list[i] = num_list[i-1] + num_list[i-2]

# print(num_list[n]%10007)


n = int(input())

num_list = [0] * (1001)
num_list[1] = 1
num_list[2] = 3
num_list[3] = 5
num_list[4] = 11
for i in range(5, n+1):
    num_list[i] = num_list[i-1] + num_list[i-2]

print(num_list[n]%10007)
