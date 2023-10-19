# 16953, A --> B, 실버2

import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int, input().split())
visited = {} # 방문한 적이 있는 값을 남기기 위한 공간

# 가능한 연산은 2가지
# 1) 2를 곱한다     2) 1의 수를 가장 오른쪽에 추가한다

queue = deque() # queue 객체 생성
queue.appendleft(A)
visited[A] = 1

while len(queue) != 0:
    cur_num = queue.pop()
    cur_move = visited[cur_num]
    
    if cur_num == B:
        break
    if (visited.get(cur_num * 10 + 1, 0) == 0) and (cur_num * 10 + 1 <= B):
        visited[cur_num * 10 + 1] = cur_move + 1
        queue.appendleft(cur_num * 10 + 1)
        
    if (visited.get(cur_num * 2, 0) == 0) and (cur_num * 2 <= B):
        visited[cur_num * 2] = cur_move + 1
        queue.appendleft(cur_num * 2)
    
if cur_num == B:
    print(cur_move)
else:
    print(-1)