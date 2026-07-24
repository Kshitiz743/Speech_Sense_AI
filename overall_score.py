def overall_score(fluency,
                 confidence,
                 fillers):


    score=0

    score+=fluency*0.40

    score+=confidence*0.40


    score+=(100-(fillers*5))*0.20


    if score>100:

        score=100


    return round(score)