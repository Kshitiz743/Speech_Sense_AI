from speech_to_text import speech_to_text

from speech_analysis import (
        total_words,
        calculate_wpm
        )

from filler_words import count_fillers

from pause_detection import (
        get_duration,
        pause_count
        )

from fluency_score import fluency_score

from confidence_score import confidence_score

from tone_analysis import tone_analysis

from overall_score import overall_score

from speech_grade import speech_grade

from ai_suggestions import suggestions



def analyze_speech(filepath):

    # Speech Recognition

    text = speech_to_text(filepath)


    # Duration

    duration = get_duration(filepath)


    # Total Words

    words = total_words(text)


    # WPM

    wpm = calculate_wpm(
            words,
            duration
            )


    # Pauses

    pauses = pause_count(duration)


    # Fillers

    fillers = count_fillers(text)


    # Fluency Score

    fluency = fluency_score(
            wpm,
            fillers,
            pauses
            )


    # Confidence Score

    confidence = confidence_score(
            wpm,
            pauses,
            fillers
            )


    # Tone Analysis

    tone = tone_analysis(wpm)


    # Overall Score

    score = overall_score(
            fluency,
            confidence,
            fillers
            )


    # Speech Grade

    grade = speech_grade(score)


    # Suggestions

    tips = suggestions(
            score,
            fillers,
            wpm
            )


    results = {

        "text":text,

        "duration":duration,

        "words":words,

        "wpm":wpm,

        "pauses":pauses,

        "fillers":fillers,

        "fluency":fluency,

        "confidence":confidence,

        "tone":tone,

        "overall":score,

        "grade":grade,

        "suggestions":tips

        }


    return results