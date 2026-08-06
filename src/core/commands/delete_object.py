from src.core.commands.base import Command


class DeleteObjectCommand(Command):

    def execute(self, controller, data):

        controller.delete_object(
            name=data["name"]
        )