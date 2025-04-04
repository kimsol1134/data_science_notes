'''
원으로 생각
12시에 있는 사람이 인덱스 0
12시에 있는 사람 제거 후 뒤에 붙이기
k-1 번째 인덱스 제거
'''
from queue import Queue

q = Queue()
N, K = map(int,input().split())
answer = []
for i in range(1, N+1):
    q.put(i)
while q.qsize() != 0 :
    for _ in range(K-1):
        a = q.get(0)
        q.put(a)
    answer.append(q.get(0))

def print_list_as_string(lst):
    elements = ", ".join(str(item) for item in lst)    
    return "<" + elements + ">"

result = print_list_as_string(answer)
print(result)