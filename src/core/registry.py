from src.core.commands.create_sphere import CreateSphereCommand
from src.core.commands.create_cube import CreateCubeCommand
from src.core.commands.create_cylinder import CreateCylinderCommand
from src.core.commands.move_object import MoveObjectCommand
from src.core.commands.rotate_object import RotateObjectCommand
from src.core.commands.scale_object import ScaleObjectCommand
from src.core.commands.delete_object import DeleteObjectCommand

COMMANDS = {
    ("create", "sphere"): CreateSphereCommand,
    ("create", "cube"): CreateCubeCommand,
    ("create", "cylinder"): CreateCylinderCommand,

    ("move", "object"): MoveObjectCommand,
    ("rotate", "object"): RotateObjectCommand,
    ("scale", "object"): ScaleObjectCommand,
    ("delete", "object"): DeleteObjectCommand
}