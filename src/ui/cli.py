import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.core.parser import CommandParser
from src.core.executor import CommandExecutor

class BlenderCLI:
    def __init__(self):
        self.parser = CommandParser()
        self.executor = CommandExecutor()

    def run(self):
        print("========== Blender Copilot ==========")
        print("Type 'exit' to quit.\n")

        self.executor.controller.clear_scene()

        while True:
            command = input(">>> ")

            if command.lower() == "exit":
                break

            try:
                parsed = self.parser.parse(command)

                self.executor.execute(parsed)

                print("✓ Done")

            except Exception as e:
                print(f"Error: {e}")