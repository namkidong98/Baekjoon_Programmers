def solution(arr, queries):
    ans = arr.copy()
    
    for query in queries:
        s, e, k = query
        for i in range(len(arr)):
            if (s <= i <= e) and (i % k == 0):
                ans[i] += 1
        
    return ans