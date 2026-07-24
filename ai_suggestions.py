def suggestions(score,fillers,wpm):

    tips=[]


    if score>90:

        tips.append(
        "Excellent speaking skills."
        )


    if fillers>3:

        tips.append(
        "Reduce filler words."
        )


    if wpm<90:

        tips.append(
        "Increase your speaking pace."
        )


    elif wpm>180:

        tips.append(
        "Speak slightly slower."
        )


    if len(tips)==0:

        tips.append(
        "Maintain your current speaking style."
        )


    return tips