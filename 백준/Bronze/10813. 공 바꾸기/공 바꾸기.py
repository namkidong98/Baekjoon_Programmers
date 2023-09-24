N, M = map(int, input().split())

ans = [_ for _ in range(N + 1)] # 초기값으로 해당 인덱스가 들어있는 0번부터 N번까지의 바구니 생성

for _ in range(M): # M번 반복
    i, j = map(int, input().split()) # 바꿀 두 바구니 선택
    ans[i], ans[j] = ans[j], ans[i] # swap

for i in ans[1:]: # 맨 앞의 0번째 바구니는 제외
    print(i, end=' ')