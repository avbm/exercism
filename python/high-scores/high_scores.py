from copy import deepcopy

def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    temp_scores = deepcopy(scores)
    temp_scores.sort()
    #temp_scores.reverse()
    ret_val = temp_scores[ -1* min(len(scores), 3):]
    ret_val.reverse()
    return ret_val
