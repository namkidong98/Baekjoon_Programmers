def solution(n, numlist):
    ans = []
    for i in numlist:
        if i % n == 0:
            ans.append(i)
    return ans