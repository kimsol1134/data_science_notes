import heapq

def getMinForce(weights) :
    '''
    n개의 점토를 하나로 합치기 위해 필요한 힘의 합의 최솟값을 반환하는 함수를 작성하세요.
    '''
    # 1. 힙으로 바꾼다.
    # 2. 가장 작은거 2개 빼서 더한다
    # 3. 다시 힙에 넣는다.
    # 4. 반복
    result = []
    heapq.heapify(weights)
    while len(weights) != 1:
        a1 = heapq.heappop(weights)
        a2 = heapq.heappop(weights)
        a3 = a1 + a2
        result.append(a3)
        heapq.heappush(weights, a3)
    
  

    return sum(result)

n = int(input())

line = [int(x) for x in input().split()]

print(getMinForce(line))