import sys
from collections import deque
input = sys.stdin.readline

def BFS(start):    
    queue = deque([1])
    visited[1] = 0 # 주사위 던진 횟수의 초기값은 0

    while(len(queue) != 0): # 큐가 빌때까지
        cur_pos = queue.popleft() # 큐에서 현재 시행의 위치를 가져오고
        cur_num_roll = visited[cur_pos] # 현재 위치까지 도달하는데 던진 주사위 횟수를 가져온다
        
        if cur_pos == 100: # 목표 지점에 도착하면 주사위 횟수 출력하고 종료
            print(visited[cur_pos])
            break;
        
        for dice_num in range(1, 7): # 주사위가 1~6까지 나올 수 있음
            next_pos = cur_pos + dice_num
        
            if next_pos <= 100 and visited[next_pos] == 0: # 범위 안에 있고 방문한 적이 없는 곳이면
                # 큐에 추가하기 전에 ladder과 snake 여부에 따라 이동을 해야 함
                if next_pos in snake.keys():
                    next_pos = snake[next_pos]   # 딕셔너리의 key를 이용해 value를 얻어서 next_pos를 갱신
                elif next_pos in ladder.keys():
                    next_pos = ladder[next_pos]  # 딕셔너리의 key를 이용해 value를 얻어서 next_pos를 갱신
                if visited[next_pos] == 0: # 여전히 다음 이동할 곳이 방문한 적이 없는 곳이라면
                    visited[next_pos] = cur_num_roll + 1
                    queue.append(next_pos)

N, M = map(int, input().split())
snake = dict(); ladder = dict()
visited = [0] * 101 # 1~100번까지 방문 여부 및 방문 차례(주사위 굴린 횟수)

for _ in range(N):
    start, end = map(int, input().split())
    ladder[start] = end
for _ in range(M):
    start, end = map(int, input().split())
    snake[start] = end
    
BFS(1)