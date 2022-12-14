import os
from pathlib import Path

import tomli

with open(Path(os.curdir) / "pyproject.toml", 'r') as f:
    config = tomli.loads(f.read())

__version__ = config['tool']['poetry']['version']
