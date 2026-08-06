import math
import bpy


class BlenderController:
    """
    Handles all interactions with Blender through the bpy API.
    """

    # SCENE

    def clear_scene(self):
        """Delete all objects from the current scene."""
        bpy.ops.object.select_all(action="SELECT")
        bpy.ops.object.delete(use_global=False)


    # CREATE OBJECTS

    def create_cube(
        self,
        size: float = 2,
        location=(0, 0, 0),
        name: str | None = None,
    ):
        bpy.ops.mesh.primitive_cube_add(
            size=size,
            location=location
        )

        obj = bpy.context.active_object

        if name:
            obj.name = name

        return obj

    def create_sphere(
        self,
        radius: float = 1,
        location=(0, 0, 0),
        name: str | None = None,
    ):
        bpy.ops.mesh.primitive_uv_sphere_add(
            radius=radius,
            location=location
        )

        obj = bpy.context.active_object

        if name:
            obj.name = name

        return obj

    def create_cylinder(
        self,
        radius: float = 1,
        depth: float = 2,
        location=(0, 0, 0),
        name: str | None = None,
    ):
        bpy.ops.mesh.primitive_cylinder_add(
            radius=radius,
            depth=depth,
            location=location
        )

        obj = bpy.context.active_object

        if name:
            obj.name = name

        return obj


    # OBJECT OPERATIONS

    def move_object(
        self,
        name: str,
        x: float = 0,
        y: float = 0,
        z: float = 0,
    ):
        obj = self.get_object(name)

        obj.location = (x, y, z)

        return obj

    def rotate_object(
        self,
        name: str,
        x: float = 0,
        y: float = 0,
        z: float = 0,
    ):
        obj = self.get_object(name)

        obj.rotation_euler = (
            math.radians(x),
            math.radians(y),
            math.radians(z),
        )

        return obj

    def scale_object(
        self,
        name: str,
        x: float = 1,
        y: float = 1,
        z: float = 1,
    ):
        obj = self.get_object(name)

        obj.scale = (x, y, z)

        return obj

    def delete_object(self, name: str):
        obj = self.get_object(name)

        bpy.data.objects.remove(obj, do_unlink=True)


    # HELPERS

    def get_object(self, name: str):
        """
        Returns a Blender object by name.
        Raises an exception if the object does not exist.
        """
        obj = bpy.data.objects.get(name)

        if obj is None:
            raise ValueError(f"Object '{name}' not found.")

        return obj

    def object_exists(self, name: str) -> bool:
        return bpy.data.objects.get(name) is not None

    def list_objects(self):
        return [obj.name for obj in bpy.data.objects]