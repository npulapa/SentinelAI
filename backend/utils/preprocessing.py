import re

def clean_text(text: str):

    text = text.lower()
    text = re.sub(r"http\S+", "", text)   # remove URLs
    text = re.sub(r"[^a-z0-9\s]", "", text)

    return text
