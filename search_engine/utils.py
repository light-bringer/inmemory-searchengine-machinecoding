import collections
import typing


def get_words_from_sentence(content: str) -> typing.List[str]:
    result = content.split()
    return result


def get_unique_words_from_sentence(content: str) -> typing.List[str]:
    return list(set(get_words_from_sentence(content)))


def get_frequency_of_words(content: str) -> typing.Dict:
    words = get_words_from_sentence(content)
    return collections.Counter(words)
