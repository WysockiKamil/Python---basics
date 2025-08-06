import os

def text_analyzer(text):
    words = text.split()
    num_words = len(words)
    num_chars = len(text)
    num_sentences = text.count('.') + text.count('!') + text.count('?')

    word_counts = {}
    for word in words:
        normalized = word.lower()
        word_counts[normalized] = word_counts.get(normalized, 0) + 1

    return {
        'num_words': num_words,
        'num_chars': num_chars,
        'num_sentences': num_sentences,
        'word_counts': word_counts
    }


def get_text_from_user():
    choice = input("Wybierz tryb (1 - wpisz tekst ręcznie, 2 - wczytaj z pliku): ").strip()
    
    if choice == '1':
        return input("Podaj tekst do analizy:\n")
    
    elif choice == '2':
        filepath = input("Podaj ścieżkę do pliku tekstowego: ").strip()
        if not os.path.isfile(filepath):
            print("Plik nie istnieje. Spróbuj ponownie.")
            return get_text_from_user()
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    
    else:
        print("Nieprawidłowy wybór. Wybierz 1 lub 2.")
        return get_text_from_user()


def main():
    user_text = get_text_from_user()
    result = text_analyzer(user_text)

    print("\n--- Wyniki analizy ---")
    print(f"Liczba słów: {result['num_words']}")
    print(f"Liczba znaków: {result['num_chars']}")
    print(f"Liczba zdań: {result['num_sentences']}")
    print("\nCzęstotliwość słów:")
    for word, count in sorted(result['word_counts'].items(), key=lambda item: item[1], reverse=True):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
