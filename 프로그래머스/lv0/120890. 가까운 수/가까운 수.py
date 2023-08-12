def solution(array, n):
    array.sort()
    min = 100; ans = 0
    for i in array:
        if abs(i - n) < min:
            min = abs(i - n)
            ans = i
    return ans
            