from src.core.commands.base import Command


class ScaleObjectCommand(Command):

    def execute(self, controller, data):

        controller.scale_object(
            name=data["name"],
            x=data.get("x", 1),
            y=data.get("y", 1),
            z=data.get("z", 1)
        )