def solution(l, r):
    ans = []
    for i in range(l, r+1):
        if all(num in ['0', '5'] for num in str(i)):
            ans.append(i)
    if len(ans) == 0:
        ans.append(-1)
    return ans