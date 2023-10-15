import sys
input = sys.stdin.readline

N = int(input()) # 최대 사용할 수 있는 회의의 수
job_list = []    # job의 시작과 끝 시간을 저장하는 리스트
for _ in range(N):
    start, end = map(int, input().split())
    job_list.append([end, start]) # 정렬을 end 기준으로 할 것이기 때문에 순서를 바꾸어서 저장
    
job_list.sort() # 첫 번째 원소들로 오름차순 정렬 

job_cnt = 1 # 첫번째 일이 계산되고
end_time = job_list[0][0] # 첫번째 일의 끝나는 시간을 추가

for idx in range(1, N): # job_list의 2번째 원소부터 가능한지 계산 
    if job_list[idx][1] >= end_time:
        job_cnt += 1
        end_time = job_list[idx][0]
    else: # 지금 작업의 끝나는 시간보다 일찍 시작하는 일들은 pass
        continue 

print(job_cnt)