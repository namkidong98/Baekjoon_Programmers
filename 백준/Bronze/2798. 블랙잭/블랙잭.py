N, M = map(int, input().split())
num_list = list(map(int, input().split()))
cur_max = 0 # 답을 저장하는 변수
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if num_list[i] + num_list[j] + num_list[k] <= M:
                cur_max = max(cur_max, num_list[i] + num_list[j] + num_list[k]) # 더 큰 값으로 cur_max 갱신
            else:
                continue # M보다 큰 경우에는 패스

print(cur_max)