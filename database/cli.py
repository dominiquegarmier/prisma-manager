import subprocess
from pathlib import Path

from argparse import ArgumentParser, Namespace


__all__ = [
    'build',
    'codegen',
]


def build(args: Namespace) -> None:
    base_path = Path(__file__).parent
    with (
        open(base_path / './prisma/schema.prisma', 'w') as dest,
        open(base_path / './prisma/models.prisma', 'r') as models,
        open(base_path / f'./prisma/{args.language}.prisma', 'r') as client,
    ):
        # remove first line that contains generator for linting
        models_strs = models.readlines()[4:]
        client_strs = client.readlines()
        dest.writelines(client_strs + models_strs)
    print(f'{args.language} client schema built at database/prisma/schema.prisma')
    return


def codegen(args: Namespace) -> None:
    build(Namespace(language='python'))
    subprocess.run(
        [
            'prisma',
            'generate',
            f'--schema={str(Path(__file__).parent / "./prisma/schema.prisma")}',
        ]
    )
    print('client generated at database/client')
    return


def main() -> int:
    parser = ArgumentParser(description='build schema for desired client')

    subparsers = parser.add_subparsers(dest='command', required=True)

    build_parser = subparsers.add_parser('build', help='build schema')
    build_parser.add_argument('language', choices=['python', 'javascript'])
    build_parser.set_defaults(func=build)

    codegen_parser = subparsers.add_parser('codegen', help='codegen schema')
    codegen_parser.set_defaults(func=codegen)

    args = parser.parse_args()
    args.func(args)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
