from __future__ import annotations


class SchemaManagerException(Exception):
    ...


class InvalidConfig(SchemaManagerException):
    ...


class ConfigNotFound(SchemaManagerException):
    ...
