def latest(scores):
    latest = scores[-1]
    return latest


def personal_best(scores):
    best = max(scores)
    return best


def personal_top_three(scores):
    sorted_scores = sorted(scores, reverse = True)
    top_three = sorted_scores[:3]
    return top_three