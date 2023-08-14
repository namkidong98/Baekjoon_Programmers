def solution(array):
    ans = 0
    for i in array:
        ans += list(str(i)).count('7')
    return ans