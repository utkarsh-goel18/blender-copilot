from src.core.commands.create_sphere import CreateSphereCommand
from src.core.commands.create_cube import CreateCubeCommand
from src.core.commands.create_cylinder import CreateCylinderCommand

COMMANDS = {

    ("create", "sphere"): CreateSphereCommand(),

    ("create", "cube"): CreateCubeCommand(),

    ("create", "cylinder"): CreateCylinderCommand(),
}