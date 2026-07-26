def tone_analysis(wpm):
    if wpm < 90:
        return "Calm"
    elif wpm < 140:
        return "Professional"
    elif wpm < 180:
        return "Energetic"
    else:
        return "Very Fast"