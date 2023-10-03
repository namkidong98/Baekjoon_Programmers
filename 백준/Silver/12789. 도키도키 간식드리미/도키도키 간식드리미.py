import sys
from collections import deque

input = sys.stdin.readline # input함수 재정의

N = int(input().rstrip())                              # 학생 수
cur_list = deque()
temp = list(map(int, input().rstrip().split()))
for x in temp:     # 학생들의 번호
    cur_list.append(x)

stack = deque() # 한 명씩만 설 수 있는 공간(stack 구조)

cur = 1 # 시작은 1번부터
flag = "Nice"
while cur <= N:
    if (len(cur_list) != 0 ) and (cur_list[0] == cur):
        cur_list.popleft() # 앞부분을 pop
        cur += 1 # 제대로 시행되었으면 cur을 1증가 시킴
    elif (len(stack) != 0) and (stack[-1] == cur):
        stack.pop() # 맨 위에서 pop
        cur += 1 # 제대로 시행되었으면 cur을 1증가 시킴
    else:
        if len(cur_list) == 0: # 기존 줄에서 1명 빼려 했는데 이미 줄에 남은 사람이 없으면
            flag = "Sad"       # 해답이 없다
            break
        stack.append(cur_list.popleft()) # 기존 줄에서 1명을 빼서 stack에 넣는다

print(flag)