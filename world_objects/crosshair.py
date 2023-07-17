from settings import *
from meshes.quad_mesh import QuadMesh

class Crosshair:
    def __init__(self, app):
        self.app = app
        self.mesh = QuadMesh(self.app)

    def update(self):
        pass

    def render(self):
        self.mesh.render()