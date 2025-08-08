import pytest
from text_analyzer import get_text_from_user

@pytest.mark.parametrize("choice, input_text, expected_output", [
    ('1', 'Hello world.', {
        "num_words": 2,
        "num_chars": 12,
        "num_sentences": 1,
        "word_counts": {"hello": 1, "world": 1}
    }),
    ('1', '', {
        "num_words": 0,
        "num_chars": 0,
        "num_sentences": 0,
        "word_counts": {}
    }),
    ('1', 'One word', {
        "num_words": 2,
        "num_chars": 8,
        "num_sentences": 0,
        "word_counts": {"one": 1, "word": 1}
    }),
    ('1', 'Multiple words with different cases.', {
        "num_words": 5,
        "num_chars": 36,
        "num_sentences": 1,
        "word_counts": {"multiple": 1, "words": 1, "with": 1, "different": 1, "cases": 1}
    })
])
def test_get_text_from_user(monkeypatch, choice, input_text, expected_output):
    if choice == '1':
        monkeypatch.setattr('builtins.input', lambda _: input_text)
    elif choice == '2':
        monkeypatch.setattr('builtins.input', lambda _: 'test_file.txt')
        with open('test_file.txt', 'w', encoding='utf-8') as f:
            f.write(input_text)

    result = get_text_from_user()
    assert result['num_words'] == expected_output['num_words']
    assert result['num_chars'] == expected_output['num_chars']
    assert result['num_sentences'] == expected_output['num_sentences']
    assert result['word_counts'] == expected_output['word_counts']