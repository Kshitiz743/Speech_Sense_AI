def speech_grade(score):
    if score>=95:
        return "MASTER SPEAKER"
    elif score>=90:
        return "EXCELLENT SPEAKER"
    elif score>=80:
        return "PROFESSIONAL SPEAKER"
    elif score>=70:
        return "GOOD SPEAKER"
    elif score>=60:
        return "AVERAGE SPEAKER"
    elif score>=50:
        return "BEGINNER SPEAKER"
    else:
        return "NEEDS IMPROVEMENT"