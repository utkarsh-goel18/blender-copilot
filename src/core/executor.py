from src.blender.controller import BlenderController
from src.core.registry import COMMANDS

class CommandExecutor:

    def __init__(self):
        self.controller = BlenderController()

    def execute(self, command_dict):
        key = (
            command_dict["action"],
            command_dict["object"],
        )
from src.blender.controller import BlenderController
from src.core.registry import COMMANDS


class CommandExecutor:

    def __init__(self):
        self.controller = BlenderController()

    def execute(self, command_dict):

        key = (
            command_dict["action"],
            command_dict["object"]
        )

        if key not in COMMANDS:
            raise ValueError(f"Unknown command: {key}")

        command_class = COMMANDS[key]
        command = command_class()

        command.execute(
            self.controller,
            command_dict
        )
        if key not in COMMANDS:
            raise ValueError(f"Unknown Command: {key}")

        command_class = COMMANDS[key]
        command = command_class()

        command.execute(
            self.controller,
            command_dict
        )