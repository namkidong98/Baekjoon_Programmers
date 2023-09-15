import numpy as np

def solution(my_string, m, c):
    data = np.array(list(my_string)).reshape(-1, m)
    row, col = data.shape
    ans = ''
    for i in range(row):
        ans += data[i][c-1]
    return ans
    