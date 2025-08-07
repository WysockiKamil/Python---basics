import pytest
from text_analyzer import text_analyzer

@pytest.mark.parametrize("input_text, expected_output", [
    ("Hello world.", {
        "num_words": 2,
        "num_chars": 12,
        "num_sentences": 1,
        "word_counts": {"hello": 1, "world": 1}
    }),
    ("", {
        "num_words": 0,
        "num_chars": 0,
        "num_sentences": 0,
        "word_counts": {}
    }),
    ("One word", {
        "num_words": 2,
        "num_chars": 8,
        "num_sentences": 0,
        "word_counts": {"one": 1, "word": 1}
    }),
    ("Multiple words with different cases.", {
        "num_words": 5,
        "num_chars": 36,
        "num_sentences": 1,
        "word_counts": {"multiple": 1, "words": 1, "with": 1, "different": 1, "cases": 1}
    })
])
def test_text_analyzer(input_text, expected_output):
    result = text_analyzer(input_text)
    assert result['num_words'] == expected_output['num_words']
    assert result['num_chars'] == expected_output['num_chars']
    assert result['num_sentences'] == expected_output['num_sentences']
    assert result['word_counts'] == expected_output['word_counts']