import bpy

class BLENDERCOPILOT_PT_MainPanel(bpy.types.Panel):

    bl_label = "Blender Copilot"
    bl_idname = "BLENDERCOPILOT_PT_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Copilot"

    def draw(self, context):
        layout = self.layout
        props = context.scene.blender_copilot
        layout.label(text="Enter command")
        layout.prop(props, "command", text="")
        layout.operator("blender_copilot.execute", text="Execute")