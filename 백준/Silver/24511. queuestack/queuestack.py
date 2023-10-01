import sys
from collections import deque

input = sys.stdin.readline  # input 함수를 재정의

N = int(input())                             # 자료 구조의 개수
dt_list = list(map(int, input().split()))    # 각 자료구조가 Queue(0)인가 Stack(1)인가
cur_list = list(map(int, input().split()))   # 각 자료구조의 초기값
M = int(input())                             # 삽입할 원소의 개수
input_list = list(map(int, input().split())) # 삽입할 M길이의 원소들

new_list = [] # queue만 저장할 새로운 리스트

res = deque()

for idx in range(N):
    if dt_list[idx] == 0:
        res.appendleft(cur_list[idx])

for idx in range(M):
    res.append(input_list[idx])
    print(res.popleft(), end=' ')

# for idx in range(N):
#     if dt_list[idx] == 0:
#         new_list.append(cur_list[idx])

# for idx in range(M):
#     cur_input = input_list[idx] # 이번 시행에 삽입할 원소
#     new_list.insert(0, cur_input) # queue의 좌측에 add queue
#     print(new_list.pop(), end=' ') # queue의 우측에서 deque