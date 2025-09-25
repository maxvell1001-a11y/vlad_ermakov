from .formatter import capitalize_text

def count_words(text):
    return len(capitalize_text(text).split())