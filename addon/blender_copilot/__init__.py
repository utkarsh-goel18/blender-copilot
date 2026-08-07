bl_info = {
    "name": "Blender Copilot",
    "author": "Utkarsh Goel",
    "version": (0, 1, 0),
    "blender": (5, 2, 0),
    "location": "View3D > Sidebar",
    "description": "Control Blender using commands",
    "category": "3D View",
}

import bpy

from .panels import BLENDERCOPILOT_PT_MainPanel
from .operators import BLENDERCOPILOT_OT_ExecuteCommand
from .properties import BlenderCopilotProperties

classes = (
    BlenderCopilotProperties,
    BLENDERCOPILOT_OT_ExecuteCommand,
    BLENDERCOPILOT_PT_MainPanel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.blender_copilot = bpy.props.PointerProperty(
        type=BlenderCopilotProperties
    )

def unregister():

    del bpy.types.Scene.blender_copilot

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()