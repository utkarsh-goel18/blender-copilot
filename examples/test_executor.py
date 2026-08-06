import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.core.parser import CommandParser
from src.core.executor import CommandExecutor

parser = CommandParser()
executor = CommandExecutor()

command = "create sphere radius=1"

parsed = parser.parse(command)

executor.controller.clear_scene()

executor.execute(parsed)

print("Command executed successfully.")