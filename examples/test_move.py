import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.core.parser import CommandParser
from src.core.executor import CommandExecutor

parser = CommandParser()
executor = CommandExecutor()

# Clear the scene
executor.controller.clear_scene()

# Create a cube named "table"
parsed = parser.parse("create cube name=table")
executor.execute(parsed)

# Move the cube
parsed = parser.parse("move object name=table x=5 y=2 z=1")
executor.execute(parsed)

print("Move test completed!")