class Tree:
    def __init__(self, i, l, r):
        self.index = i # 노드의 value
        self.left = l
        self.right = r
    def addNode(self, i, l, r):
        if self.index == None or self.index == i:
            self.index = i
            if l < i :
                self.left = Tree(l, None, None) if l != None else None # l이 None 이면 None,None,None 노드 추가되는거 막음
            if r > i :
                self.right = Tree(r,None,None) if r != None else None
            return True
        else : #현재 노드가 비어있지 않거나 지금 인덱스랑 다를때 왼쪽 노드부터 탐색
            if self.left != None:
                if self.left.addNode(i, l, r) == True: #좌측노드 인덱스에서 탐색
                    return True
                if self.right.addNode(i, l, r) == True:
                    return True
                return False

# 전위 순회 리스트로 넣기
def preorder(tree):
    result = []
    result.append(tree.index) # 1. 루트 먼저
    if tree.left != None:
        result += preorder(tree.left) # 왼쪽 자식 노드가 있으면 방문
    if tree.right != None:
        result += preorder(tree.right) # 오른쪽 자식 노드가 있으면 방문
    return result

# 전위 순회 한 값을 보고 트리를 만든다
# 첫번째 루트
# 두번째 값이 첫번째 값보다 작으면 좌측 자식
# 크면 우측 자식
# 재귀
# 다시 후위 순회 한다.
import sys

nodes = []
while True:
    try:
        line = input()
        # 빈 줄이 입력되면 반복 종료
        if line == "":
            break
        # 입력된 문자열을 정수로 변환하여 리스트에 추가
        nodes.append(int(line))
    except ValueError:
        # 숫자가 아닌 값이 입력되면 오류 메시지 출력 후 계속 진행
        print("잘못된 입력입니다. 숫자를 입력해주세요.")
    except EOFError:
        # 파일 끝(EOF)에 도달하면 종료 (터미널 환경에 따라 발생 가능)
        break
# def reverse_preorder(nodes):
#     result = [0]*len(nodes)
#     result[0] = nodes[0]
#     for i in range(1,len(nodes)):
#         if nodes[i] < nodes[i-1]:
#             result[i]

print(preorder(nodes))



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