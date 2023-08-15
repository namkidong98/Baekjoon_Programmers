def solution(sides):
    result = 0
    # case1: 가장 긴 변이 이미 sides에 있을 때
    result += len(range(max(sides) - min(sides) + 1, max(sides) + 1))
    
    # case2: 가장 긴 변이 추가되는 경우
    result += len(range(max(sides) + 1, sum(sides)))
    return result