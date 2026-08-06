from src.core.commands.base import Command


class CreateCubeCommand(Command):

    def execute(self, controller, data):

        controller.create_cube(
            size=data.get("size", 2),
            location=data.get("location", (0, 0, 0))
        )