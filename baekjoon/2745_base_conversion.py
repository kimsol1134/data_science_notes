def char_to_num(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')        
    elif 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 10 

n, b = input().split()
n = n[::-1]
b = int(b)
ans = []
for i in n :
    ans.append(char_to_num(i))

i = 0
result = 0
while i < len(ans) :
    result +=ans[i]*(b**i)
    i +=1
print(result)
