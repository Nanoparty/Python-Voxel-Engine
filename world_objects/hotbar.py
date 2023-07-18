from settings import *
from meshes.hotbar_mesh import HotBarMesh
from meshes.hotbar_icon_mesh import HotBarIconMesh

class HotBar:
    def __init__(self, voxel_handler):
        self.app = voxel_handler.app
        self.handler = voxel_handler
        self.hotbar_mesh = HotBarMesh(self.app)
        self.hotbar_icon_mesh = HotBarIconMesh(self.app)

    def update(self):
        pass

    def set_uniform(self):
        self.hotbar_icon_mesh.program['voxel_id'] = self.handler.new_voxel_id

    def render(self):
        self.set_uniform()
        self.hotbar_icon_mesh.render()
        self.hotbar_mesh.render()