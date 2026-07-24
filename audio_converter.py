from pydub import AudioSegment



def convert_audio(filepath):


    if filepath.endswith(".webm"):


        audio = AudioSegment.from_file(

                    filepath,

                    format="webm"

                    )


        wav_path = filepath.replace(

                        ".webm",

                        ".wav"

                        )


        audio.export(

                wav_path,

                format="wav"

                )


        return wav_path



    return filepath