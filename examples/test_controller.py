import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.blender.controller import BlenderController


controller = BlenderController()

controller.clear_scene()

controller.create_cube(
    size=2,
    location=(0, 0, 0)
)

controller.create_sphere(
    radius=1,
    location=(3, 0, 0)
)

controller.create_cylinder(
    radius=1,
    depth=3,
    location=(-3, 0, 0)
)

print("Blender Copilot controller working!")