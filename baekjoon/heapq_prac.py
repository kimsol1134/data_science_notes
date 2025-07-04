import heapq

heap = [5,3,10,7]

heapq.heappush(heap, 1)
heapq.heappush(heap, 4)
heapq.heappush(heap, 3)
heapq.heappush(heap, 2)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))

heapq.heapify(heap) # 원래 리스트를 우선순위 힙으로 
print(heap)