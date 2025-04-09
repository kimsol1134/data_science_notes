list = [0]*31
for i in range(1,29):
    n = int(input())
    list[n] = n
for i in range(1,31):
    if list[i] == 0 :
        print(i)