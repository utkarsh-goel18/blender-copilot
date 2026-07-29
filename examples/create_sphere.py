import bpy

# Delete everything in the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

#Create a UV Sphere
bpy.ops.mesh.primitive_uv_sphere_add(
    radius = 1,
    location = (0, 0, 0)
)

print("Sphere created successfully!")
