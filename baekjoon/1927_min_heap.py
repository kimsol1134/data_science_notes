n = int(input())

class PriorityQueue:

    def __init__(self) :
        self.data = [0] # 인덱스 1부터 사용하기 위해 인덱스0 에 더미 변수

    def push(self, value) :
        '''
        우선순위 큐에 value를 삽입합니다.
        '''
        self.data.append(value)
        index = len(self.data) -1
        
        while index != 1: # 마지막 삽입값이 루트노드(index=1)되면 반복문 종료
            if self.data[index//2] > self.data[index] : #부모노드의 값이 자식노드보다 크다면
                temp = self.data[index]
                self.data[index] = self.data[index//2] #자식노드랑 부모노드 교환
                self.data[index//2] = temp
                index = index // 2 #인덱스 부모노드로 
            else : #부모노드의 값이 자식노드보다 작으면 종료
                break
    def pop(self) :
        if len(self.data) <= 1 :
            print(0)
            return
        else :
            print(self.data[1])

        self.data[1] = self.data[-1]
        self.data.pop()
        cur_idx = 1

        while True:
            left, right = cur_idx *2 , cur_idx *2 +1
            smallest = cur_idx
            if left < len(self.data) and self.data[left] < self.data[smallest]:
                smallest = left
            if right < len(self.data) and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == cur_idx :
                break
            self.data[cur_idx],self.data[smallest] = self.data[smallest], self.data[cur_idx]
            cur_idx = smallest
heapq = PriorityQueue()

for _ in range(n):
    num = int(input())
    if num == 0:
        heapq.pop()
    else :
        heapq.push(num)
