import wave
def get_duration(filepath):
    with wave.open(filepath, "rb") as audio:
        frames = audio.getnframes()
        rate = audio.getframerate()
        duration = frames / float(rate)
    return round(duration,2)

def pause_count(duration):
    if duration < 30:
        return 1
    elif duration < 60:
        return 2
    elif duration < 120:
        return 4
    else:
        return 6