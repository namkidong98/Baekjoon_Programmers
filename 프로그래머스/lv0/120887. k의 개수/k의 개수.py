def solution(i, j, k):
    k = str(k)
    result = 0
    for num in range(i, j + 1):
        num = list(str(num))
        result += num.count(k)
    return result