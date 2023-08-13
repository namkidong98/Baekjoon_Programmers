def solution(array):
    for i in range(len(array)):
        if array[i] == max(array):
            return [max(array), i]