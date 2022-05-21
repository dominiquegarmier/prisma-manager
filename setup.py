from __future__ import annotations

import subprocess

from setuptools import setup


def install_npm_deps() -> None:
    subprocess.call(['npm', 'install'])


setup()
