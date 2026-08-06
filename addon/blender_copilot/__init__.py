bl_info = {
    "name": "Blender Copilot",
    "author": "Utkarsh Goel",
    "version": (0, 1, 0),
    "blender": (5, 2, 0),
    "location": "View3D",
    "description": "AI-powered Blender assistant",
    "category": "Development",
}

import bpy


class COPILOT_OT_Test(bpy.types.Operator):

    bl_idname = "copilot.test"

    bl_label = "Copilot Test"

    def execute(self, context):

        self.report({'INFO'}, "Blender Copilot Loaded!")

        print("Blender Copilot Loaded!")

        return {'FINISHED'}


def menu_func(self, context):

    self.layout.operator(COPILOT_OT_Test.bl_idname)


def register():

    bpy.utils.register_class(COPILOT_OT_Test)

    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():

    bpy.types.VIEW3D_MT_object.remove(menu_func)

    bpy.utils.unregister_class(COPILOT_OT_Test)


if __name__ == "__main__":
    register()