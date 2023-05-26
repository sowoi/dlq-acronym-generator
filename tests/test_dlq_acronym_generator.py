import pytest
import os
import os.path
from dlq_acronym_generator.dlq_acronym_generator import (
    read_words_from_file,
    choose_word,
    check_last_word,
    generate_acronym,
)


@pytest.fixture
def words_fixture():
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(project_dir)
    D_Words = read_words_from_file(os.path.join(
        project_dir, "dlq_acronym_generator/D_Words.txt"))
    D_Words_Verbs = read_words_from_file(os.path.join(
        project_dir, "dlq_acronym_generator/D_Words_Verbs.txt"))
    L_Words = read_words_from_file(os.path.join(
        project_dir, "dlq_acronym_generator/L_Words.txt"))
    L_Words_Verbs = read_words_from_file(os.path.join(
        project_dir, "dlq_acronym_generator/L_Words_Verbs.txt"))
    Q_Words = read_words_from_file(os.path.join(
        project_dir, "dlq_acronym_generator/Q_Words.txt"))

    return {
        "D_Words": D_Words,
        "D_Words_Verbs": D_Words_Verbs,
        "L_Words": L_Words,
        "L_Words_Verbs": L_Words_Verbs,
        "Q_Words": Q_Words,
    }


def test_read_words_from_file():
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    words_file_path = os.path.join(project_dir, "tests", "test_words.txt")
    words = read_words_from_file(words_file_path)
    assert len(words) == 3
    assert words == ["apple", "banana", "cherry"]


def test_choose_word(words_fixture):
    D_Word, L_Word, Q_Word, D_Word_Verb, L_Word_Verb = choose_word(
        **words_fixture)
    assert D_Word in words_fixture["D_Words"]
    assert L_Word in words_fixture["L_Words"]
    assert Q_Word in words_fixture["Q_Words"]
    assert D_Word_Verb in words_fixture["D_Words_Verbs"]
    assert L_Word_Verb in words_fixture["L_Words_Verbs"]


def test_check_last_word():
    assert check_last_word("word/m", "verb", is_verb=True) == "verb"
    assert check_last_word("word/w", "verb", is_verb=True) == "verb"
    assert check_last_word("word/s", "verb", is_verb=True) == "verb"
    assert check_last_word("word/m", "noun", is_verb=False) == "nouner"
    assert check_last_word("word/w", "noun", is_verb=False) == "noune"
    assert check_last_word("word/s", "noun", is_verb=False) == "nounes"
    assert check_last_word("other", "word") == "word"


def test_generate_acronym(words_fixture, capsys):
    acronyms = generate_acronym()
    assert len(acronyms) == 5


if __name__ == "__main__":
    pytest.main()
