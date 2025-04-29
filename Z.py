import sys # sys 모듈 임포트 (빠른 입력을 위해)

result = 0 # 최종 결과(방문 순서)를 저장할 변수, 0부터 시작

# 재귀 함수 sol 정의
# n: 현재 탐색 중인 정사각형의 한 변의 길이
# x: 현재 탐색 중인 정사각형의 시작 행(row) 좌표
# y: 현재 탐색 중인 정사각형의 시작 열(column) 좌표
def sol(n, x, y):
    global result # 전역 변수 result를 함수 내에서 사용(값을 변경하기 위함)

    # 1. 종료 조건: 찾으려는 좌표 (r, c)에 도달했을 때
    # 현재 정사각형의 시작점 (x, y)가 목표 좌표 (r, c)와 같다면,
    # 현재까지 누적된 result 값이 바로 (r, c)의 방문 순서임
    if x == r and y == c:
        print(int(result)) # 결과 출력 (n/2 연산 때문에 float가 될 수 있어 int로 변환)
        # sys.exit(0) # 프로그램을 완전히 종료하고 싶다면 이 줄을 사용해도 됩니다.
        return # 함수 종료

    # 2. 최적화(Pruning): 현재 탐색 영역에 목표 좌표 (r, c)가 없는 경우
    # 만약 목표 좌표 (r, c)가 현재 탐색 중인 정사각형 [x, x+n), [y, y+n) 범위 밖에 있다면,
    # 이 정사각형 전체를 건너뛰어야 함.
    if not (x <= r < x+n and y <= c < y + n):
        # 현재 정사각형의 모든 칸의 개수 (n*n) 만큼 result에 더해줌
        # (이 칸들은 목표 좌표보다 먼저 방문되므로)
        result += n*n
        return # 더 이상 이 영역을 탐색할 필요가 없으므로 함수 종료

    # 3. 분할 정복: 현재 정사각형을 4개의 사분면으로 나누어 탐색
    # (위의 1, 2번 조건에 해당하지 않으면, 목표 좌표는 반드시 현재 정사각형 내부에 있음)
    # 한 변의 길이를 절반으로 줄임 (n/2)

    # Z 순서대로 각 사분면을 재귀적으로 탐색
    # 3-1. 왼쪽 위 사분면 탐색
    sol(n/2, x, y)
    # 3-2. 오른쪽 위 사분면 탐색
    sol(n/2, x, y + n/2)
    # 3-3. 왼쪽 아래 사분면 탐색
    sol(n/2, x + n/2, y)
    # 3-4. 오른쪽 아래 사분면 탐색
    sol(n/2, x + n/2, y + n/2)

# 입력 받기
n, r, c = map(int, sys.stdin.readline().split())

# 함수 호출 시작
# 초기 호출: 전체 배열 (크기 2^n x 2^n, 시작점 (0, 0)) 로 시작
sol(1 << n, 0, 0) # 1 << n 은 2의 n제곱 (2^n)을 의미하는 비트 연산



n = 2
r, c = 3,1

size = 2**n
count = 0
z_map = [[0]* size for _ in range(size)]

def fill_z(x, y, size):
    global count
    if size ==1 :
        z_map[x][y] = count
        count += 1
        return
    
    half = size//2

    fill_z(x, y, half)
    fill_z(x, y + half, half)
    fill_z(x + half, y, half)
    fill_z(x + half, y + half, half)


fill_z(0,0, size)


