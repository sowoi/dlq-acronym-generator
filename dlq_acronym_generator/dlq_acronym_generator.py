import random
import logging
import re
import os
from typing import List, Dict, Tuple


logging.basicConfig(level=logging.WARNING)


def read_words_from_file(file_path: str) -> List[str]:
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    words_file_path = os.path.join(
        project_dir, "dlq_acronym_generator", file_path)
    with open(words_file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]


def choose_word(
    **kwargs: Dict[str, List[str]]
) -> Tuple[str, str, str, str, str]:
    D_Words = kwargs.get("D_Words")
    L_Words = kwargs.get("L_Words")
    Q_Words = kwargs.get("Q_Words")
    D_Words_Verbs = kwargs.get("D_Words_Verbs")
    L_Words_Verbs = kwargs.get("L_Words_Verbs")
    D_Word = random.choice(D_Words)
    L_Word = random.choice(L_Words)
    Q_Word = random.choice(Q_Words)
    D_Words_Verb = random.choice(D_Words_Verbs)
    L_Words_Verb = random.choice(L_Words_Verbs)
    return D_Word, L_Word, Q_Word, D_Words_Verb, L_Words_Verb


def check_last_word(word: str, words: str, is_verb: bool = False) -> str:
    if word.endswith("/m"):
        if not words[0].isupper() and not is_verb:
            return f"{words}er"
    elif word.endswith("/w"):
        if not words[0].isupper() and not is_verb:
            return f"{words}e"
    elif word.endswith("/s"):
        if not words[0].isupper() and not is_verb:
            return f"{words}es"
    return words


def generate_acronym() -> List[str]:
    DLQ_result: List[str] = []
    D_Words: List[str] = read_words_from_file("D_Words.txt")
    logging.info(D_Words)
    D_Words_Verbs: List[str] = read_words_from_file("D_Words_Verbs.txt")
    logging.info(D_Words_Verbs)
    L_Words: List[str] = read_words_from_file("L_Words.txt")
    logging.info(L_Words)
    L_Words_Verbs: List[str] = read_words_from_file("L_Words_Verbs.txt")
    logging.info(L_Words_Verbs)
    Q_Words: List[str] = read_words_from_file("Q_Words.txt")
    logging.info(Q_Words)
    L_Word_Verb: str = ""
    D_Word_Verb: str = ""
    while len(DLQ_result) < 5:
        word_dict: Dict[str, List[str]] = {
            "D_Words": D_Words,
            "L_Words": L_Words,
            "Q_Words": Q_Words,
            "D_Words_Verbs": D_Words_Verbs,
            "L_Words_Verbs": L_Words_Verbs
        }
        D_Word, L_Word, Q_Word, _, _ = choose_word(**word_dict)

        while D_Word[0].isupper() and L_Word[0].isupper():
            D_Word, L_Word, _, _, _ = choose_word(**word_dict)
        while L_Word[0].isupper() and Q_Word[0].isupper():
            _, L_Word, Q_Word, _, _ = choose_word(**word_dict)

        if D_Word[0].isupper() and Q_Word[0].isupper():
            _, _, _, _, L_Word_Verb = choose_word(**word_dict)
            L_Word = L_Word_Verb
        elif L_Word[0].isupper():
            _, _, _, D_Word_Verb, _ = choose_word(D_Words_Verbs)
            D_Word = D_Word_Verb

        last_word = (
            Q_Word if Q_Word[0].isupper() else
            L_Word if L_Word[0].isupper() else
            D_Word if D_Word[0].isupper() else
            ""
        )

        L_Word = check_last_word(last_word, L_Word, L_Word == L_Word_Verb)
        Q_Word = check_last_word(last_word, Q_Word)
        D_Word = check_last_word(last_word, D_Word, D_Word == D_Word_Verb)

        DLQ_Acronym = re.sub(r"(/w|/m|/s)", "", f"{D_Word} {L_Word} {Q_Word}")
        logging.info(DLQ_Acronym)
        DLQ_result.append(DLQ_Acronym)

    return DLQ_result


def main():
    result = generate_acronym()
    for dlq in result:
        print(f"{dlq} (DLQ)")


if __name__ == "__main__":
    main()
