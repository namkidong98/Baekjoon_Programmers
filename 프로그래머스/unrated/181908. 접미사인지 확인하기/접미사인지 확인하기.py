def solution(my_string, is_suffix):
    if is_suffix not in my_string:
        return 0
    else:
        if my_string[-len(is_suffix):] == is_suffix:
            return 1
        else:
            return 0