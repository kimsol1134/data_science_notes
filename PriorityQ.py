class PriorityQueue:
    def __init__(self):
        self.data = [0] # 인덱스를 1부터 사용하기 위해 0번째 인덱스에 아무값 넣음
    def push(self, value):
        self.data.append(value)
        index = len(self.data) -1 

        while index != 1: # 마지막 삽입값이 index==1(루트노드)가 되면 반복문 종료
            if self.data[index//2] > self.data[index] #부모 노드 인덱스n , 자식노드 2n, 2n+1 완전이진트리, 부모노드의 값이 자식 노드보다 크면 최소힙이므로 값 바꿔야함
                self.data[index//2], self.data[index] = self.data[index], self.data[index//2]
                index = index//2 #부모노드,자식노드 값 바꾸고 인덱스를 부모 노드로 바꿔서 반복함
            else : #부모노드의 값이 자식노드보다 작으면 좋료
                break
    
    