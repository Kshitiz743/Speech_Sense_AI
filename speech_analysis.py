def total_words (text):
    words=text.split()
    return len(words)
def speech_duration(seconds):
    return round(seconds,2)
def calculate_wpm(words, duration):
    if duration==0:
        return 0
    minutes=duration/60
    return round(words/minutes)

