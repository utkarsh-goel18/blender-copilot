from src.core.commands.base import Command

class CreateSphereCommand(Command):
    def execute(self, controller, data):
        controller.create_sphere(
            radius=data.get("radius", 1),
            location=data.get("location", (0, 0, 0)),
            name=data.get("name")
        )