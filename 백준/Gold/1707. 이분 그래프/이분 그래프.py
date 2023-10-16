import sys
from collections import deque
input = sys.stdin.readline

def BFS(start_vertex):
    queue = deque()
    queue.appendleft(start_vertex)
    visited[start_vertex] = 1
    
    flag = True # 이분 그래프인지 아닌지를 판별하는 변수
    while(len(queue) != 0 and flag):
        cur_vertex = queue.pop()
        cur_level = visited[cur_vertex]
        
        for next_vertex in edge_list[cur_vertex]:
            if visited[next_vertex] == 0: # 방문한 적이 없는 노드라면
                visited[next_vertex] = cur_level * (-1) # 현재 노드와는 다른 색으로 칠하고
                queue.appendleft(next_vertex)
            elif visited[next_vertex] != 0: # 방문한 적이 있는 노드라면, 다른 색인지 체크
                if visited[cur_vertex] * visited[next_vertex] > 0: # 같은 색이라면
                    flag = False # 이분 그래프가 아니라는 지표를 남기고
                    break;       # for문 종료
    
    return flag
                
K = int(input()) # 테스트 케이스 개수
for _ in range(K):
    V, E = map(int, input().split()) # 정점의 개수, 간선의 개수
    edge_list = [[] for _ in range(V+1)] # 1~V개까지
    visited = [0] * (V+1)                # 방문 기록 겸 color을 표시(1 or -1)
    
    # 간선의 정보 입력 받기
    for _ in range(E):
        a, b = map(int, input().split())
        edge_list[a].append(b)
        edge_list[b].append(a)
    
    # 이분 그래프 검사
    result = True
    for vertex in range(1, V+1): # 비연결 그래프일 수도 있으니 모든 vertex에 대해 검사
        if visited[vertex] == 0:
            result = result and BFS(vertex) # 기존 result와 and 논리연산(모두 True일 때만 True 유지)
    
    # 결과 출력
    print("YES") if result else print("NO")