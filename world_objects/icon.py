from settings import *
from meshes.hotbar_icon_mesh import HotBarIconMesh

class Icon:
    def __init__(self, voxel_handler, voxel_id=1, vertical=0):
        self.app = voxel_handler.app
        self.handler = voxel_handler
        self.icon_mesh = HotBarIconMesh(self.app, y=vertical)
        self.voxel_id = voxel_id;

    def update(self):
        pass

    def set_uniform(self):
        self.icon_mesh.program['voxel_id'] = self.voxel_id

    def render(self): 
        self.set_uniform()
        self.icon_mesh.render()