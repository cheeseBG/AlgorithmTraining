# Greedy Problem:
# If we have positive integer set,find the minimum positive integer
# which can't define with integer set.

weight = [3, 1, 6, 2, 7, 30, 1]

# Sorting(ascending)
weight.sort()


def solution(w_list):
    result = w_list.pop(0) + w_list.pop(0)

    while w_list != []:
        if result < w_list[0] and result + 1 < w_list[0]:
            return result + 1
        else:
            result += w_list.pop(0)

    return result + 1


solution(weight)
