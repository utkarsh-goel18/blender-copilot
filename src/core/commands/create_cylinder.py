from src.core.commands.base import Command

class CreateCylinderCommand(Command):
    def execute(self, controller, data):
        controller.create_cylinder(
            radius=data.get("radius", 1),
            depth=data.get("depth", 2),
            location=data.get("location", (0, 0, 0)),
            name=data.get("name")
        )