from settings import *
from world import World
from world_objects.voxel_marker import VoxelMarker
from world_objects.crosshair import Crosshair
from meshes.quad_mesh import QuadMesh
from world_objects.hotbar import HotBar

class Scene:
    def __init__(self, app):
        self.app = app
        self.world = World(self.app)
        self.voxel_marker = VoxelMarker(self.world.voxel_handler)
        self.quad_mesh = QuadMesh(self.app)
        self.hotbar = HotBar(self.world.voxel_handler)

    def update(self):
        self.world.update()
        self.voxel_marker.update()
        self.hotbar.update()

    def render(self):
        self.world.render()
        self.voxel_marker.render()
        self.quad_mesh.render()
        self.hotbar.render()
        