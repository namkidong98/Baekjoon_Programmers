import sys
sys.setrecursionlimit(100001) # 최대 vertex의 개수만큼 DFS가 들어갈 수 있기 때문에 재귀 제한을 증대
input = sys.stdin.readline

def DFS(vertex):
    global order
    
    # 방문 기록 남기기
    visited[vertex] = order
    order += 1 # 다음 vertex의 방문 차례를 위해 1 증가
    
    for next_vertex in edge_list[vertex]:
        if visited[next_vertex] == 0: # 아직 방문하지 않은 vertex라면
            DFS(next_vertex)          # 그 vertex를 시작점으로 DFS를 재귀적 호출

N, M, R = map(int, input().split())
edge_list = [[] for _ in range(N+1)] # 각 vertex를 인덱스로 하여 해당 vertex가 연결된 vertex를 저장하는 edge list를 빈 리스트로 확보
visited = [0] * (N+1) # 각 vertex를 인덱스로 하여 해당 vertex의 방문 여부 및 차례를 저장하는 리스트
order = 1             # 방문 차례

for _ in range(M):
    a, b = map(int, input().split())
    edge_list[a].append(b)
    edge_list[b].append(a)
for vertex in range(1, N+1):
    edge_list[vertex] = sorted(edge_list[vertex], reverse=True) # 내림차순으로 원소를 정렬

DFS(R) # 지정된 시작 vertex로 DFS를 시작
for vertex in range(1, N+1):
    print(visited[vertex])