import argparse
from argparse import ArgumentParser as Parser, Namespace as Args
import re


def cli() -> Args:
    parser = Parser('squerdle', description='A tool for cheating Wordle.')

    parser.add_argument('-c', '--contains',
                        help='a string of letters of unknown'
                        ' position that are in the word.',
                        type=list,)

    parser.add_argument('-v', '--does-not-contain',
                        help='a string of letters that are not'
                        ' in the word.',
                        type=list)

    parser.add_argument('--contains-at', '--ck',
                        help='Key-value pairs (e.g., a=1) that'
                        ' indicate that a letter is present at'
                        ' a specific position.',
                        nargs='*',
                        type=parse_kv,)

    parser.add_argument('--does-not-contain-at', '--vk',
                        help='The inverse of `--kv`, indicates'
                        ' a letter is *not* at the given position.',
                        nargs='*',
                        type=parse_kv,)

    args = parser.parse_args()

    return args


def parse_kv(s: str) -> tuple[str, int]:
    if not re.match(r'^[a-z]=[1-5]$', s):
        raise argparse.ArgumentTypeError(f'Invalid format: {s}. Must of form a=b, where a'
                                         ' is any lowercase letter and b is a number 1-5.')
    key, value = s.split('=')
    return key, int(value)
