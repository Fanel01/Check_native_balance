import os
import sys

from pathlib import Path


if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.absolute()

WALLETS_DIR = os.path.join(ROOT_DIR, './data/wallets.txt')