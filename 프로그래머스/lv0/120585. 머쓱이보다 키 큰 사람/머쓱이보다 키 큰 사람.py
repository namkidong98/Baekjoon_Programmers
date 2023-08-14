def solution(array, height):
    array.append(height) # 기존 리스트에 머쓱이 키를 추가
    dic = {} # 빈 딕셔너리 만들기
    for idx, tall in enumerate(sorted(array)): # 정렬한 리스트에서 인덱스와 키 조합을
        dic[tall] = idx                        # 딕셔너리에 key와 value로 추가
    return len(array) - (dic[height] + 1) # 전체 인원의 수 - 머쓱이의 순서