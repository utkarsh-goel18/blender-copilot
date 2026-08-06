import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.ui.cli import BlenderCLI

cli = BlenderCLI()

cli.run()