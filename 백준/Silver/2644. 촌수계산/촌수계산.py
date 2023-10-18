# 2644 촌수계산, 실버2

import sys
from collections import deque
input = sys.stdin.readline

def BFS(start, end):
    queue = deque()
    queue.appendleft(start)
    visited[start] = 0
    
    while len(queue) != 0:
        cur_vertex = queue.pop()
        cur_distance = visited[cur_vertex] 

        if cur_vertex == end:   # 다른 사람에 도달하면
            return cur_distance # 계산된 촌수를 반환

        for next_vertex in Edge_list[cur_vertex]:
            if visited[next_vertex] == 0:               # 방문하지 않은 정점이면
                visited[next_vertex] = cur_distance + 1 # 촌수를 1개씩 늘리면서 저장
                queue.appendleft(next_vertex)
    
    return -1           
        

V = int(input()) # 전체 인원 수(Vertex의 개수)
X, Y = map(int, input().split()) # 촌수를 계산해야 하는 두 명
E = int(input()) # 전체 관계의 수(Edge의 개수)

Edge_list = [[] for _ in range(V+1)] # 1~V까지
visited = [0] * (V+1)

for _ in range(E):
    a, b = map(int, input().split())
    Edge_list[a].append(b)
    Edge_list[b].append(a)

ans = BFS(X, Y)
print(ans)