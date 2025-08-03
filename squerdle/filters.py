from argparse import Namespace as Args
from typing import Callable


def filter_from_args(args: Args) -> list[Callable[[str], bool]]:
    filters = []

    if args.contains:
        filters.append(must_contain(args.contains))

    if args.does_not_contain:
        filters.append(must_not_contain(args.does_not_contain))

    if args.contains_at:
        filters.append(must_have_at(args.contains_at))

    if args.does_not_contain_at:
        filters.append(mustnt_have_at(args.does_not_contain_at))

    return filters


def must_contain(letters: list[str]) -> Callable[[str], bool]:
    '''Create a filter that requires that certain letters contained in the word.'''
    return lambda word: all(letter in word for letter in letters)


def must_not_contain(letters: list[str]) -> Callable[[str], bool]:
    '''Create a filter that requires that certain letters not be contained in the word.'''
    return lambda word: all(letter not in word for letter in letters)


def must_have_at(letter_pos: list[tuple[str, int]]) -> Callable[[str], bool]:
    '''Create a filter that requires that letters be at a certain position in the word.'''
    return lambda word: all(word[pos - 1] == letter for letter, pos in letter_pos)


def mustnt_have_at(letter_pos: list[tuple[str, int]]) -> Callable[[str], bool]:
    '''Create a filter that requires that letters not be at a certain position in the word.'''
    return lambda word: all(word[pos - 1] != letter for letter, pos in letter_pos)
