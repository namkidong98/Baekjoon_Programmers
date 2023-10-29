# 1926 그림, 실버1
import sys
from collections import deque
input = sys.stdin.readline

def BFS(i, j):
    queue = deque()
    queue.appendleft((i, j))
    visited[i][j] = 1
    cnt = 1
    # up, right, down, left
    move_x = [-1, 0, 1, 0] # 행 기준 움직임
    move_y = [0, 1, 0, -1] # 열 기준 움직임
    
    
    while len(queue) != 0:
        x, y = queue.pop()
        
        for idx in range(4):
            next_x = x + move_x[idx]
            next_y = y + move_y[idx]
            if next_x >= 0 and next_x < N and next_y >= 0 and next_y < M: # 범위 안에 있으면서
                if matrix[next_x][next_y] and visited[next_x][next_y] == 0: # 아직 방문하지 않았으면
                    queue.appendleft((next_x, next_y)) # 큐에 넣고
                    visited[next_x][next_y] = 1 # 방문 기록 남기기
                    cnt += 1 # 넓이를 증가
    return cnt

N, M = map(int, input().split())
matrix = []
visited = []
for i in range(N):
    line = list(map(int, input().split()))
    matrix.append(line)
    visited.append([0 for _ in range(M)]) 

max = 0 # 가장 넓은 그림의 넓이
num = 0 # 그림의 개수
for i in range(N):
    for j in range(M):
        if matrix[i][j] and visited[i][j] == 0: # 1인데 방문하지 않은 곳이면
            num += 1
            result = BFS(i, j)
            if result > max:
                max = result

print(num)
print(max)