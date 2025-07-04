from queue import Queue

def BFS(tree):
    q= Queue()
    result = []
    q.put(tree)
    while not q.empty():
        cur = q.get()
        if cur == None :
            continue
        result.append(cur.index)
        q.put(cur.left)
        q.put(cur.right)
    return result



# 어떤 트리의 루트 노드를 갖고 있다.
class Tree:
    def __init__(self, i, l, r) :
        self.index = i
        self.left = l
        self.right = r
    # 재귀적으로 동작한다.
    # 새로운 노드가 현재 노드의 자식으로 추가되어야 하는 경우
    # -> 바로 추가.
    # 그렇지 않다면, 자기 자식 중에 새로운 노드를 받을 수 있는 노드를 탐색 -> 재귀 알고리즘
    def addNode(self, i, l, r) :
        '''
        트리 내의 정점 i에 대하여 왼쪽자식을 l, 오른쪽 자식을 r로
        설정해주는 함수를 작성하세요.
        '''
        if self.index == None or self.index == i : #트리의 현재 노드 인덱스와 i가 일치할때 (혹은 비어있을때)
            self.index = i #self.index ==None 일때 i로 
            self.left = Tree(l, None, None) if l != None else None #이렇게 해야 Tree(None, None, None)이렇게 추가되는거 막음
            self.right = Tree(r, None, None) if r != None else None         
            return True   
        else :
            if self.left != None:
                if self.left.addNode(i, l, r) == True:
                    return True
            if self.right != None:
                if self.right.addNode(i, l, r) == True:
                    return True
            return False
        


def getHeight(myTree):
    if myTree == None :
        return 0
    else :
        return 1 + max(getHeight(myTree.left), getHeight(myTree.right))
    return 0





class PriorityQueue:
    '''
    우선순위 큐를 힙으로 구현합니다
    '''

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
        '''
        우선순위가 가장 높은 원소를 제거합니다.
        '''
        if len(self.data) == 1 : # 0번 인덱스만 있을때
            return
        
        self.data[1] = self.data[-1] #루트와 마지막 노드 교환
        self.data.pop() #마지막 노드 제거합니다
        index = 1 #루트 인덱스0
        # 부모가 자식보다 작을때 까지 교환
        while True :
            priority = -1 #둘중 교환할 인덱스(왼쪽,오른쪽,둘다 아님)
            left_child_index = index * 2 
            right_child_index = index*2 +1

            # 1. 왼쪽 자식노드가 없는 경우는 오른쪽 자식도 무조건 없으므로 리프노드
            if len(self.data) - 1 < left_child_index:
                break
            # 2. 왼쪽 자식만 있는경우
            elif len(self.data) - 1 < right_child_index : 
                priority = left_child_index # 왼쪽 자식만 있으므로 왼쪽 자식을 바꿔줄 후보로 넣음
            # 3. 양쪽 자식 다 있는 경우
            else :    # 둘중 더 작은 값을 바꿔줄 후보로 넣음
                if self.data[left_child_index] < self.data[right_child_index]:
                    priority = left_child_index
                else :
                    priority = right_child_index
            
            # 선택된 후보 자식이 현재 노드보다 작으면 교환
            if self.data[index] > self.data[priority]:
                temp = self.data[index]
                self.data[index] = self.data[priority] #자식노드랑 부모노드 교환
                self.data[priority] = temp
            else :
                break

    def top(self) :
        '''
        우선순위가 가장 높은 원소를 반환합니다. 만약 우선순위 큐가 비어있다면 -1을 반환합니다.
        '''
        if len(self.data) == 1 : # 0번 인덱스만 있을때
            return -1
        return self.data[1]
    

import heapq

class PriorityQueue:
    def __init__(self):
        self.data = []
    def push(self, value):
        heapq.heappush(self.data,(abs(value),value))
    def pop(self):
        if len(self.data)>0:
            heapq.heappop(self.data)
    def top(self):
        if len(self.data) == 0:
            return -1
        else :
            return self.data[0][1]
        
def heapSort(items):
    result = []
    pq = PriorityQueue()

    for item in items:
        pq.push(item)
    for i in range(len(items)):
        result.append(pq.top())
        pq.pop()
    return result



import heapq

def find_mid(nums) :
    '''
    n개의 정수들을 담고 있는 배열 nums가 매개변수로 주어집니다.
    nums의 각 정수들이 차례대로 주어질 때, 매 순간마다 
    "지금까지 입력된 수 중에서 중간값"을 리스트로 저장하여 반환하세요.
    '''
    n = len(nums)
    result = [] # 각 단계의 중간값
    less = [] # 중간값이 루트, 중간값보다 작거나 같은 값, 최대힙
    greater = [] # 중간값보다 큰 값들, 최소힙

    for i in range(n):
        x = nums[i] # 현재 숫자
        # 힙이 비어있는 경우 최대힙에 삽입
        if  not less or not greater :
            heapq.heappush(less, -x)
        else : # 중간값과 대소비교
            if x >= -less[0]:
                heapq.heappush(greater, x)
            else :
                heapq.heappush(less, -x)
        while not (len(less)==len(greater) or len(less) == len(greater)+1):
            if len(less) > len(greater):
                heapq.heappush(greater, -heapq.heappop(less))
            else :
                heapq.heappush(less, -heapq.heappop(greater))
        result.append(-less[0])
    return result

#  less -> 최대힙에 저장
# greater -> 최소힙에 저장
# less의 루트노드 보다 작은수가 입력되면 최대힙에 저장
# 아니면 최소힙에 저장
# 최대힙의 루트노드가 중간값이 되도록
# 최소힙의 갯수가 최대힙보다 많아지면 최소힙의 루트노드를 최대힙으로 보냄