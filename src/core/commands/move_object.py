from src.core.commands.base import Command


class MoveObjectCommand(Command):

    def execute(self, controller, data):

        controller.move_object(
            name=data["name"],
            x=data.get("x", 0),
            y=data.get("y", 0),
            z=data.get("z", 0)
        )