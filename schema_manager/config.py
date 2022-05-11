from __future__ import annotations

from functools import cache
from typing import TypedDict

import yaml


class PackageMetadata(TypedDict):
    name: str
    version: str
    author: str
    email: str


class SchemaMetadata(TypedDict):
    schema_path: str
    clients: list[ClientMetadata]


class ClientMetadata(TypedDict):
    id: str
    language: str
    path: str


class Config(TypedDict):
    package_metadata: PackageMetadata
    schema_metadata: SchemaMetadata


class InvalidConfig(Exception):
    pass


@cache
def load_config(config_path: str | None = None) -> Config | None:
    try:
        with open(config_path or '.prisma-schema-manager.yaml') as f:
            parsed_config = yaml.safe_load(f)['config']

        package = parsed_config['package']
        package_metadata: PackageMetadata = {
            'name': package.get('name', 'name'),
            'version': package.get('version', '0.0.1'),
            'author': package.get('author', 'author'),
            'email': package.get('email', 'example@email.com'),
        }

        schema = parsed_config['schema']
        clients: list[ClientMetadata] = []
        schema_metadata: SchemaMetadata = {
            'schema_path': schema['schema_path'],
            'clients': clients,
        }
        for client in schema['clients']:
            client_md: ClientMetadata = {
                'id': client['id'],
                'language': client['language'],
                'path': client['path'],
            }
            clients.append(client_md)

        return {
            'package_metadata': package_metadata,
            'schema_metadata': schema_metadata,
        }
    except (KeyError, IndexError):
        raise InvalidConfig()
