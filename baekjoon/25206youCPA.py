g_dic = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0
}
sum_j = 0
len_j = 0

for i in range(20):
    a_list= [v for v in input().split()]
    if a_list[2] == "P":
        pass
    else:
        jum = g_dic[a_list[2]]
        sum_j += jum * float(a_list[1])
        len_j += float(a_list[1])
print(sum_j/len_j)