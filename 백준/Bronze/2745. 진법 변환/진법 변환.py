number, base = input().split()
power_list = [_ for _ in range(len(number))][::-1] # number의 자리수에 따라 곱해줘야 하는 제곱수를 저장한 리스트
alpha_num = dict(list(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(10, 36)))) # 알파벳과 10~35를 zip으로 각각 묶어주고 리스트로 변환하고 딕셔너리화한다

sum = 0
idx = 0

for num in number: # number로 들어온 문자열을 앞에서부터 읽는다
    # 문자를 숫자로 변환
    if num.isalpha(): # 10 이상이면 딕셔너리 이용
        num = alpha_num[num]
    else: # 10 이하이면 그대로 int형 변환
        num = int(num)
    # 기존 sum에 합산
    sum += (int(base) ** power_list[idx]) * num
    idx += 1 # 다음 인덱스

print(sum)