from __future__ import annotations

import os
import subprocess
from pathlib import Path

from database.commands.switch import _switch


def reset_db() -> None:
    # switch to js client
    schema_path = Path(__file__).parent / 'prisma/schema.prisma'
    _switch('javascript')
    subprocess.call(['npx', '-y', 'migrate', 'reset', '--schema', str(schema_path)])
