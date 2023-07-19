from settings import *
from meshes.base_mesh import BaseMesh
from array import array

class InventoryMesh(BaseMesh):
    def __init__(self, app):
        super().__init__()

        self.app = app;
        self.ctx = app.ctx
        self.program = app.shader_program.inventory

        self.vbo_format = '3f 3f'
        self.attrs = ('in_position', 'tex_coords',)
        self.vao = self.get_vao()

    def get_vertex_data(self):

        length = 0.1 * ASPECT_RATIO
        vertices = [
            (.6, .5, 0.0), (-.6, .5, 0.0), (-.6, -.5, 0.0),
            (.6, .5, 0.0), (-.6, -.5, 0.0), (.6, -.5, 0.0)
        ]
        tex_coords = [
            (1, 1, 0), (0, 1, 0), (0, 0, 0),
            (1, 1, 0), (0, 0, 0), (1, 0, 0)
        ]

        vertex_data = np.hstack([vertices, tex_coords], dtype='float32')
        return vertex_data