import librosa


def get_duration(filepath):

    duration = librosa.get_duration(path=filepath)

    return round(duration,2)



def pause_count(duration):

    # temporary logic

    if duration < 30:

        return 1

    elif duration < 60:

        return 2

    elif duration < 120:

        return 4

    else:

        return 6