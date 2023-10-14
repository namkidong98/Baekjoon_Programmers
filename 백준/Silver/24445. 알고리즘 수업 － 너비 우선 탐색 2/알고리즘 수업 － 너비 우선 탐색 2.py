import sys
from collections import deque
input = sys.stdin.readline

def update_visited(vertex):
    global order
    visited[vertex] = order
    order += 1

def BFS(start_vertex):
    queue = deque()
    queue.appendleft(start_vertex)
    update_visited(start_vertex)
    
    while(len(queue) != 0):
        cur_vertex = queue.pop()
        
        for next_vertex in edge_list[cur_vertex]:
            if visited[next_vertex] == 0:
                update_visited(next_vertex)
                queue.appendleft(next_vertex)
            else:
                continue

N, M, R = map(int, input().split())
edge_list = [[] for _ in range(N+1)] # 1~N까지 vetex의 edge 정보를 저장
visited = [0] * (N+1) # 1~N까지 vertex의 방문 여부 및 방문 차례를 저장
order = 1 # 방문 차례

for _ in range(M): # 간선의 정보 입력 받기
    a, b = map(int, input().split())
    edge_list[a].append(b)
    edge_list[b].append(a)
for vertex in range(1, N+1):
    edge_list[vertex].sort(reverse=True) # 내림차순으로 정렬
    
BFS(R) # R을 시작 노드로 BFS 시작
print(*visited[1:], sep='\n') # 결과 출력 