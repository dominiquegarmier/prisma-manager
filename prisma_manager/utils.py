from __future__ import annotations

from functools import cache
from pathlib import Path


SCHEMA_PATH = Path(__file__).parent / 'schema/'


def _init_schema_folder() -> None:
    if not SCHEMA_PATH.is_dir():
        SCHEMA_PATH.mkdir()
    return None


def _parse_schema() -> str:
    models_path = Path(__file__).parent / 'prisma/schema.prisma'
    ret = ''
    started = False
    with open(models_path) as f:
        for line in f:
            if line.startswith('datasource'):
                started = True
            if started:
                ret += line
    return ret


def _parse_client(lang: str) -> str | None:
    client_path = Path(__file__).parent / f'prisma/{lang}.prisma'
    if not client_path.is_file():
        return None
    with open(client_path) as f:
        return f.read()


@cache
def get_schema(client: str) -> Path | None:
    out_path = SCHEMA_PATH / f'{client}_schema.prisma'
    if out_path.is_file():
        return out_path

    _init_schema_folder()

    _client = _parse_client(client)
    _schema = _parse_schema()

    if _client is None:
        return None

    with open(out_path, 'w') as f:
        f.write(_client + '\n' + _schema)

    return out_path
