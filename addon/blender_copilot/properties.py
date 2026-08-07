import bpy

StringProperty = bpy.props.StringProperty


class BlenderCopilotProperties(bpy.types.PropertyGroup):

    command: StringProperty(
        name="Command",
        description="Enter a Blender Copilot command",
        default=""
    )