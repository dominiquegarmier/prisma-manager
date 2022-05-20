from __future__ import annotations

import subprocess
from argparse import Namespace
from pathlib import Path

from database.commands.switch import _switch


def _codegen() -> None:
    schema_path = Path(__file__).parent.parent / 'prisma/schema.prisma'
    subprocess.call(
        [
            'prisma',
            'generate',
            f'--schema={schema_path}',
        ]
    )
    print('client generated at database/client')
    pass


def codegen(args: Namespace) -> int:
    _switch(args.client)
    _codegen()
    return 0
