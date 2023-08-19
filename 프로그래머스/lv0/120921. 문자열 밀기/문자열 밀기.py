def push(string):
    string = list(string)
    a = string.pop() # 맨 끝을 빼냏어 a에 저장
    string.insert(0, a) # 맨 앞에 빼넣은 a를 삽입
    return ''.join(string)
    
def solution(A, B):
    if A == B:
        return 0
    
    for i in range(len(A)):
        A = push(A) # 한칸 밀어주고
        if A == B:
            return i + 1
    # for문을 빠져 나왔다면 B와 일치하는 경우가 없다는 뜻
    return -1