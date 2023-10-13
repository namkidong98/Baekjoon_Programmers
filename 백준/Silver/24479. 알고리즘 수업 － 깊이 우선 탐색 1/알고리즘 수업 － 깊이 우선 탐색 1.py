import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

def DFS(start_vertex):
    global order # order를 글로벌 변수로 활용
    
    #방문 기록 남기기
    visited[start_vertex] = order # 현재 order에 담긴 방문 차례로 visited를 업데이트
    order += 1                    # 다음 vertex를 위해 방문차례를 1개 증가
    
    for next_vertex in edge[start_vertex]:
        if visited[next_vertex] == 0: # 해당 인접 vertex를 방문할 수 있으면
            DFS(next_vertex)          # 해당 vertex 시작점으로 하여 DFS를 호출

N, M, R = map(int, input().split())
edge = [[] for _ in range(N+1)] # 1번부터 N번까지의 vertex에 대한 인접 edge를 저장하기 위한 빈 리스트 생성
visited = [0]*(N+1)             # 1번부터 N번까지의 vertex에 방문했는지 여부를 나타내는 변수(0이면 미방문, 1이상이면 방문 순서)
order = 1                       # 방문 차례를 나타내는 변수

for _ in range(M): # 주어진 간선의 개수 M 만큼 정보를 받아서 각 vertex의 edge list에 넣는다
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
for idx in range(1, N+1): # vertex별로 edge 안의 vertex들을 오름차순으로 정렬해야 한다
    edge[idx] = sorted(edge[idx]) # 인접 vertex는 오름차순으로 방문하기 때문

DFS(R)
for idx in range(1, N+1):
    print(visited[idx])