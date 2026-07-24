def fluency_score(wpm,fillers,pauses):

    score=100


    # fillers

    score-=fillers*8


    # pauses

    score-=pauses*5


    # speaking speed

    if wpm<80:

        score-=25

    elif wpm<100:

        score-=15

    elif wpm>180:

        score-=25

    elif wpm>160:

        score-=15


    if score<0:

        score=0


    if score>100:

        score=100


    return score