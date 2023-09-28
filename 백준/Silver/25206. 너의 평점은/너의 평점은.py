total_credit = 0    # 학점 총합
total_score = 0     # 전공평점 = (학점 * 과목평점)의 총합
score_dict = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0}

for i in range(20): # 20줄에 걸친 입력
    subject, credit, score = input().split()
    if score == 'P': continue # 평점이 P인 것은 제외
    total_credit += float(credit)
    total_score += float(credit) * score_dict[score] 

print("{:.6f}".format(total_score / total_credit))