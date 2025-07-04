import sys
import heapq
input = sys.stdin.readline


N = int(input())
answer = []
for _ in range(N):
    n = int(input())
    heapq.heappush(answer, n)
for i in range(len(answer)):
    print(heapq.heappop(answer))

#counting sort
def solve():
    # 숫자의 개수 N 입력 받기
    # sys.stdin.readline()은 input()보다 빠르게 입력을 받을 수 있어
    # 많은 양의 입력을 처리할 때 유리합니다.
    n = int(sys.stdin.readline())

    # 카운팅 배열 생성 (숫자 1부터 10,000까지 카운트하기 위해 크기 10001)
    # 인덱스 0은 사용하지 않습니다.
    counts = [0] * 10001

    # N개의 숫자 입력 받으며 카운팅
    for _ in range(n):
        num = int(sys.stdin.readline())
        counts[num] += 1

    # 카운팅 배열을 순회하며 결과 출력
    # 1부터 10000까지의 숫자를 확인
    for i in range(1, 10001):
        # counts[i]가 0보다 크면, 해당 숫자 i가 counts[i]번 등장했다는 의미
        if counts[i] > 0:
            # 등장한 횟수만큼 숫자 i를 출력
            for _ in range(counts[i]):
                print(i)

# 함수 실행
solve()