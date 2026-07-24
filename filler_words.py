FILLERS=[
    "um",
    "uh",
    "hmm",
    "actually",
    "basically",
    "like",
    "you know",
    "okay",
    "okay",
    "right",
    "so",

]
def count_fillers(text):
    text=text.lower()
    count=0
    words=text.split()

    for word in words:
        if word in FILLERS:
            count=count+1
    return count


