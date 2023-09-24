N, M = map(int, input().split())

ans = [_ for _ in range(N + 1)] # 0번쨰부터 N번째까지 바구니 생성

for _ in range(M): # M번 반복
    s, e = map(int, input().split()) # 역순할 바구니의 시작과 끝을 입력
    ans[s:e+1] = ans[s:e+1][::-1] # 역순으로 정렬한 것을 기존 바구니에 넣음

for i in ans[1:]: # 맨 앞의 0번째 바구니는 제외
    print(i, end=' ')