from __future__ import annotations

from argparse import Namespace
from pathlib import Path

from schema_manager.config import Config

SAMPLE_CONFIG = '''\
config:
  package:
    name: name
    version: 0.0.1
    author: author name
    email: author@example.com
  schema:
    models_path: ./prisma/models.prisma
    clients:
    - id: python
      lang: python
      path: ./prisma/python.prisma
'''


def init(args: Namespace) -> int:
    config_path: str = args.config_path or '.prisma-schema-manager.yaml'
    path = Path(args.root) / config_path
    if path.is_file():
        print(f'{path} is already a file')
        return 1
    try:
        with open(path, 'w') as f:
            f.write(SAMPLE_CONFIG)
    except FileNotFoundError:
        print(f'directory {args.root} does not exist, or was not found!')
        return 1
    return 0
