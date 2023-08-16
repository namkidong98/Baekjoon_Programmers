def solution(score):
    score = [sum(i) / 2 for i in score]
    rank = [(sorted(score, reverse=True).index(i) + 1, i) for i in score]
    return [idx for idx, value in rank]
    