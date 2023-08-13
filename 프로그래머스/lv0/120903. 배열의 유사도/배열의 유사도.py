def solution(s1, s2):
    ans = 0
    for char in s1:
        if char in s2:
            ans += 1
    return ans