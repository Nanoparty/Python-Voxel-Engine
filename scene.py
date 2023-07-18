from settings import *
from world import World
from world_objects.voxel_marker import VoxelMarker
from world_objects.crosshair import Crosshair
from meshes.quad_mesh import QuadMesh
from meshes.hotbar_mesh import HotBarMesh
from meshes.hotbar_icon_mesh import HotBarIconMesh

class Scene:
    def __init__(self, app):
        self.app = app
        self.world = World(self.app)
        self.voxel_marker = VoxelMarker(self.world.voxel_handler)
        #self.crosshair = Crosshair(app)
        self.quad_mesh = QuadMesh(self.app)
        self.hotbar = HotBarMesh(self.app)
        self.hotbaricon = HotBarIconMesh(self.app)

    def update(self):
        self.world.update()
        self.voxel_marker.update()

    def render(self):
        self.world.render()
        self.voxel_marker.render()
        self.quad_mesh.render()
        
        self.hotbaricon.render()
        self.hotbar.render()