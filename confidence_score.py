def confidence_score(wpm, pauses, fillers):
    score = 100
    # speaking pace
    if wpm < 90:
        score -= 15
    elif wpm > 180:
        score -= 15
    # pauses
    score -= pauses * 2
    # filler words
    score -= fillers * 3
    if score < 0:
        score = 0
    return score