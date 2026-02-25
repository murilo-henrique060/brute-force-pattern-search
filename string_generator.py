from lorem_text import lorem

def generate_string(length: int) -> str:
    if length <= 0:
        return ""

    text = ""

    while len(text) < length:
        text += lorem.paragraph() + '\n'

    return text[:length-1] + "."