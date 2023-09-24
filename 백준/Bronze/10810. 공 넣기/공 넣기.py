N, M = map(int, input().split())

ans = [0 for _ in range(N)] # 초기값으로 0이 들어있는 1번부터 N번까지의 바구니 생성

for _ in range(M):
    i, j, k = map(int, input().split())
    put = [k for _ in range(j - i + 1)]
    ans[i-1:j] = put

for i in ans:
    print(i, end=' ')