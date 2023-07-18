from settings import *
from meshes.base_mesh import BaseMesh
from array import array

class HotBarMesh(BaseMesh):
    def __init__(self, app):
        super().__init__()

        self.app = app;
        self.ctx = app.ctx
        self.program = app.shader_program.hotbar

        self.vbo_format = '3f 3f'
        self.attrs = ('in_position', 'tex_coords',)
        self.vao = self.get_vao()

    def get_vertex_data(self):

        length = 0.1 * ASPECT_RATIO
        vertices = [
            (0.05, -0.8, 0.0), (-0.05, -0.8, 0.0), (-0.05, -0.8 - length, 0.0),
            (0.05, -0.8, 0.0), (-0.05, -0.8 - length, 0.0), (0.05, -0.8 - length, 0.0)
        ]
        tex_coords = [
            (1, 1, 0), (0, 1, 0), (0, 0, 0),
            (1, 1, 0), (0, 0, 0), (1, 0, 0)
        ]

        vertex_data = np.hstack([vertices, tex_coords], dtype='float32')
        return vertex_data