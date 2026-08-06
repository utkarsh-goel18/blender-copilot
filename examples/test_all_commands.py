import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.core.parser import CommandParser
from src.core.executor import CommandExecutor

parser = CommandParser()
executor = CommandExecutor()

executor.controller.clear_scene()

commands = [
    "create cube name=table size=2",
    "create sphere name=ball radius=1",
    "create cylinder name=pillar radius=0.5 depth=4",

    "move object name=table x=3 y=0 z=0",
    "rotate object name=table z=45",

    "move object name=ball x=-3 y=0 z=1",
    "scale object name=ball x=2 y=2 z=2",

    "delete object name=pillar"
]

for cmd in commands:
    parsed = parser.parse(cmd)
    executor.execute(parsed)

print("All commands executed successfully!")