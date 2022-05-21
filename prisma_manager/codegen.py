from __future__ import annotations

import subprocess
from argparse import Namespace
from pathlib import Path

from prisma_manager.utils import get_schema


def _codegen(path: Path) -> None:
    subprocess.call(
        [
            'prisma',
            'generate',
            f'--schema={path}',
        ]
    )
    print('client generated')
    pass


def codegen(args: Namespace) -> int:
    schema = get_schema(args.client)
    if schema is None:
        print(f'{args.client} client not found')
        return 1
    _codegen(schema)
    return 0
