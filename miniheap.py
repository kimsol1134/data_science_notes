class PriorityQueue:
    '''
    우선순위 큐를 최소 힙(Min Heap)으로 구현합니다.
    최소 힙은 부모 노드의 값이 항상 자식 노드의 값보다 작거나 같은 완전 이진 트리입니다.
    따라서 루트 노드는 항상 전체 트리에서 가장 작은 값을 가집니다.
    '''

    def __init__(self) :
        '''
        우선순위 큐 초기화 - 인덱스를 1부터 시작하기 위해 0번 인덱스에 더미 값 추가
        self.data[0]은 사용하지 않고, 실제 데이터는 인덱스 1부터 시작합니다.
        '''
        self.data = [0]  # 0번 인덱스는 사용하지 않음 (힙에서 계산 편의를 위해)

    def push(self, value) :
        '''
        우선순위 큐에 value를 삽입합니다.
        
        1. 새 값을 배열 마지막에 추가합니다.
        2. 추가된 값을 부모 노드와 비교하여 필요시 위치를 교환합니다(상향식 재구성).
        3. 올바른 위치를 찾을 때까지 이 과정을 반복합니다.
        
        시간 복잡도: O(log n), 여기서 n은 큐의 크기입니다.
        '''
        # 1. 새 값을 배열 마지막에 추가
        self.data.append(value)
        
        # 현재 삽입된 값의 인덱스
        index = len(self.data) - 1 '''계산 더 편해지는거 맞나??'''
        
        # 2. 힙 속성 유지를 위한 상향식 재구성(upheap) 수행
        while index != 1:  # 루트 노드(인덱스 1)에 도달할 때까지
            parent_idx = index // 2  # 부모 노드의 인덱스, 자식노드가 2n , 2n+1 이므로? 이거할려고 인덱스 1부터한듯?
            
            # 부모 노드의 값이 현재 노드보다 크면 위치 교환 (최소 힙 속성 유지)
            if self.data[parent_idx] > self.data[index]:
                # 부모 노드와 현재 노드의 값을 교환
                temp = self.data[index]
                self.data[index] = self.data[parent_idx]
                self.data[parent_idx] = temp
                
                # 인덱스를 부모 노드로 이동하여 계속 검사
                index = parent_idx
            else:
                # 부모 노드가 현재 노드보다 작거나 같으면 힙 속성이 유지되므로 종료
                break


    def top(self) :
        '''
        우선순위가 가장 높은 원소(최소값)를 반환합니다.
        만약 우선순위 큐가 비어있다면 -1을 반환합니다.
        
        시간 복잡도: O(1)
        '''
        if len(self.data) == 1:  # 큐가 비어있는 경우 (0번 인덱스만 있음)
            return -1
        else:
            return self.data[1]  # 루트 노드(인덱스 1)가 최소값


    def pop(self) :
        '''
        우선순위가 가장 높은 원소(최소값)를 제거합니다.
        
        1. 루트 노드에 마지막 노드를 위치시킵니다.
        2. 마지막 노드를 제거합니다.
        3. 새 루트 노드를 자식 노드들과 비교하여 필요시 위치를 교환합니다(하향식 재구성).
        4. 올바른 위치를 찾을 때까지 이 과정을 반복합니다.
        
        시간 복잡도: O(log n), 여기서 n은 큐의 크기입니다.
        '''
        if len(self.data) == 1:  # 큐가 비어있는 경우
            return
        
        # 1. 루트 노드에 마지막 노드 위치시키기
        self.data[1] = self.data[-1]
        
        # 2. 마지막 노드 제거
        self.data.pop()
        
        # 현재 검사 중인 노드 인덱스 (루트부터 시작)
        index = 1
        
        # 3. 힙 속성 유지를 위한 하향식 재구성(downheap) 수행
        while True:
            priority = -1  # 교환할 자식 노드의 인덱스
            
            left_child_idx = index * 2
            right_child_idx = index * 2 + 1
            
            # 1) 자식 노드가 없는 경우 (리프 노드)
            if len(self.data) - 1 < left_child_idx:
                break
                
            # 2) 왼쪽 자식만 있는 경우
            elif len(self.data) - 1 < right_child_idx:
                priority = left_child_idx
                
            # 3) 양쪽 자식 모두 있는 경우, 더 작은 값을 가진 자식 선택
            else:
                if self.data[left_child_idx] < self.data[right_child_idx]:
                    priority = left_child_idx  # 왼쪽 자식이 더 작은 경우
                else:
                    priority = right_child_idx  # 오른쪽 자식이 더 작은 경우
            
            # 선택된 자식이 현재 노드보다 작으면 교환 (최소 힙 속성 유지)
            if self.data[index] > self.data[priority]:
                # 현재 노드와 선택된 자식 노드의 값 교환
                temp = self.data[index]
                self.data[index] = self.data[priority]
                self.data[priority] = temp
                
                # 인덱스를 선택된 자식 노드로 이동하여 계속 검사
                index = priority
            else:
                # 자식들이 현재 노드보다 크거나 같으면 힙 속성이 유지되므로 종료
                break