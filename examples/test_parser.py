import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.core.parser import CommandParser

parser = CommandParser()

command = "create sphere radius=2"

parsed = parser.parse(command)

print(parsed)