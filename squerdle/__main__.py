#! /usr/bin/env python3
from .cli import cli
from .filters import filter_from_args
from .words import WORDS
from .summarise import distribution


def main() -> None:
    args = cli()
    filters = filter_from_args(args)

    matches = [word for word in WORDS if all(f(word) for f in filters)]

    if args.distribution:
        print(distribution(matches))
    else:
        print('\n'.join(matches))


if __name__ == '__main__':
    main()
