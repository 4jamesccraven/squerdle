from collections import Counter
from itertools import starmap


def distribution(words: list[str]) -> str:
    all_chars = list(''.join(words))
    counts: Counter = Counter(all_chars)

    max_num_width: int = max(
        map(lambda p: len(str(p[1])), counts.most_common()))

    def fmt_count(letter: str, count: int) -> str:
        return f'{letter}: {count:>{max_num_width}}'

    lines: list[str] = list(starmap(fmt_count, counts.most_common()))

    return '\n'.join(lines)
