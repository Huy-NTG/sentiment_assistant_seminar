import underthesea

COMMON_REPLACE = {
    "rat": "rất", "ko": "không", "hok": "không",
    "zui": "vui", "bik": "biết", "dc": "được", "hom" : "hôm"
}

def normalize_text(text):
    text = text.lower()
    for k, v in COMMON_REPLACE.items():
        text = text.replace(k, v)
    return " ".join(underthesea.word_tokenize(text))
