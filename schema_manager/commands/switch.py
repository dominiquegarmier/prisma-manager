from __future__ import annotations

from argparse import Namespace
from pathlib import Path

from schema_manager.config import Config


def build(args: Namespace) -> None:
    base_path = Path(__file__).parent
    with (
        open(base_path / './prisma/schema.prisma', 'w') as dest,
        open(base_path / './prisma/models.prisma') as models,
        open(base_path / f'./prisma/{args.language}.prisma') as client,
    ):
        # remove first line that contains generator for linting
        models_strs = models.readlines()[4:]
        client_strs = client.readlines()
        dest.writelines(client_strs + models_strs)
    print(f'{args.language} client schema built at database/prisma/schema.prisma')
    return


def switch(config: Config, args: Namespace) -> int:
    return 0
