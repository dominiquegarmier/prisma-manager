from __future__ import annotations

import configparser
from argparse import Namespace
from pathlib import Path


def _parse_model() -> str:
    models_path = Path(__file__).parent.parent / 'prisma/models.schema'
    ret = ''
    started = False
    with open(models_path) as f:
        for line in f:
            if line.startswith('datasource'):
                started = True
            if started:
                ret += line
    return ret


def _parse_client(lang: str) -> str:
    client_path = Path(__file__).parent.parent / f'prisma/{lang}.schema'
    if not client_path.is_file():
        print(f'could not generate {lang} client, {client_path} not found')
        raise SystemExit(-1)
    with open(client_path) as f:
        return f.read()


def _switch(client: str) -> int:
    models_string = _parse_model()
    client_string = _parse_client(client)

    schema_path = Path(__file__).parent.parent / 'prisma/schema.prisma'

    with open(schema_path, 'w') as f:
        f.write(models_string)
        f.write('\n')
        f.write(client_string)

    print(f'built schema at {schema_path}')
    return 0


def switch(args: Namespace) -> int:
    return _switch(args.client)
