from __future__ import annotations

from argparse import ArgumentParser
from argparse import Namespace
from typing import Callable
from typing import cast

from config import Config

from database.commands.codegen import codegen
from database.commands.switch import switch


def main() -> int:

    parser = ArgumentParser('prisma schema manager')
    subparsers = parser.add_subparsers(title='commands')

    condgen_parser = subparsers.add_parser('codegen', help='generate prisma client')
    condgen_parser.add_argument('client', help='client to generate', type=str)
    condgen_parser.set_defaults(func=codegen)

    switch_parser = subparsers.add_parser('switch', help='switch client')
    switch_parser.add_argument('client', help='client to generate', type=str)
    switch_parser.set_defaults(func=switch)

    parser.add_argument(
        '--debug', help='enable debug mode', action='store_true', dest='debug'
    )

    parser.add_argument(
        '--config',
        dest='config_path',
        type=str,
        help='path to config file',
        required=False,
    )

    args = parser.parse_args()
    args.func = cast(Callable[[Namespace], int], args.func)
    return args.func(args)


if __name__ == '__main__':
    raise SystemExit(main())
