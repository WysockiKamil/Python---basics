def text_analyzer(text):
    wordss = []
    for slowo in text.split():
        if slowo.lower() not in wordss:
            wordss.append(slowo.lower())
    words = text.split()
    num_words = len(words)
    num_chars = len(text)
    num_sentences = text.count('.') + text.count('!') + text.count('?')
    
    return {
        'num_words': num_words,
        'num_chars': num_chars,
        'num_sentences': num_sentences,
        'unique_words': wordss,
        'unique_words_length': len(wordss)
    }
