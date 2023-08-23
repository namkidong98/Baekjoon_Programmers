def solution(arr, queries):
    result = []
    for s, e, k in queries:
        minimum = 1000001
        for i in arr[s:e+1]:
            if i > k and minimum > i:
                minimum = i
        result.append(minimum) if minimum != 1000001 else result.append(-1)
    return result