import sys
input = sys.stdin.readline

N = int(input())
people = [int(x) for x in input().split()] 
people.sort() # 오름차순으로 정렬
total = 0 # 총 걸리는 시간
cum = 0 # 해당 사람의 순서까지 누적된 시간
for time in people: # 각 사람마다 걸리는 시간으로
    cum += time     # 누적 시간을 갱신
    total += cum    # 전체 시간을 갱신
print(total)