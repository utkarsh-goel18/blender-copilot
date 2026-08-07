import bpy
import sys
import os

PROJECT_ROOT = r"D:\PROJECTS\Blender Copilot"

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

print("Using project root:", PROJECT_ROOT)
print(sys.path)

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
            print("=" * 50)
            print("Received:", command)

            parsed = parser.parse(command)

            print("Parsed:", parsed)

            executor.execute(parsed)

            print("Execution successful")
            print("=" * 50)

            self.report({"INFO"}, "Command Executed")

        except Exception as e:

            print("ERROR:", e)
            import traceback
            traceback.print_exc()

            self.report({"ERROR"}, str(e))