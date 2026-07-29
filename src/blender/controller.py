import bpy


class BlenderController:

    def clear_scene(self):
        """
        Removes all objects from the current Blender scene."""
        bpy.ops.object.select_all(action = 'SELECT')
        bpy.ops.object.delete()

    def create_sphere(self, radius = 1, location = (0, 0, 0)):
        """
        Creates a sphere in the current Blender scene.
        """
        bpy.ops.mesh.primitive_uv_sphere_add(
            radius = radius,
            location = location
        )

    def create_cube(self, size=2, location = (0,0,0)):
        """
        Creates a cube in the current Blender scene.
        """
        bpy.ops.mesh.primitive_cube_add(
            size = size,
            location = location
        )

    def create_cylinder(self, radius=1, depth=2, location = (0,0,0)):
        """
        Creates a cylinder in the current Blender scene.
        """
        bpy.ops.mesh.primitive_cylinder_add(
            radius = radius,
            depth = depth,
            location = location
        )