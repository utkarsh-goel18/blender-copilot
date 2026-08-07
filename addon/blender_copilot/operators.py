import bpy
import sys
import os


PROJECT_ROOT = r"D:\PROJECTS\Blender Copilot"

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from src.core.parser import CommandParser
from src.core.executor import CommandExecutor


class BLENDERCOPILOT_OT_ExecuteCommand(bpy.types.Operator):
    bl_idname = "blender_copilot.execute"
    bl_label = "Execute"

    def execute(self, context):


        command = context.scene.blender_copilot.command

        parser = CommandParser()
        executor = CommandExecutor()

        try:
            parsed = parser.parse(command)
            executor.execute(parsed)

            self.report({"INFO"}, "Command Executed")

            return {"FINISHED"}

        except Exception as e:
            self.report({"ERROR"}, str(e))
            print(e)

            return {"CANCELLED"}