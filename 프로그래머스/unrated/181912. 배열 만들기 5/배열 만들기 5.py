def solution(intStrs, k, s, l):
    ans = []
    for intStr in intStrs:
        number = int(intStr[s:s+l])
        if number > k:
            ans.append(number)
    return ans